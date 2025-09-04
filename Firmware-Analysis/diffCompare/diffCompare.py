import r2pipe
import json

path_file1      = "bootloader.bin"
base_addr_file1 = 0x08000000

path_file2      = "circuittracks-firmware-4486.bin"
base_addr_file2 = 0x08010000

def bitwise_hamming_simmilarity(b1, b2):
    length = min(len(b1), len(b2))
    if length == 0:
        raise ValueError("zero length function")
    diff_bits = 0
    for i in range(length):
        diff_bits += bin(b1[i] ^ b2[i]).count('1')
    return 1 - (diff_bits / (length * 8))



def analyze_firmware(path_to_firmware, fileoffset):
    flag_list = ['-a', 'arm', '-b', '16', '-m', "0x{:08X}".format(fileoffset)]
    r2        = r2pipe.open(path_to_firmware, flags=flag_list)
    r2.cmd('aaa')

    functions = json.loads(r2.cmd('aflj'))
    results   = []

    for func in functions:
        func_offset = func.get('offset')
        func_name   = func.get('name') or f"sub_{func_offset:x}"
        func_size   = func.get('size', 0)

        # Try to get argument count
        nargs = 0
        afij = json.loads(r2.cmd(f'afij @ {func_offset}'))
        if afij and isinstance(afij, list):
            nargs = afij[0].get('nargs', 0)

        # Disassemble function and extract calls
        calls = []
        pdfj = json.loads(r2.cmd(f'pdfj @ {func_offset}'))
        if pdfj and 'ops' in pdfj:
            for op in pdfj['ops']:
                if op.get('type') == 'call' and 'jump' in op:
                    call_addr = op['jump']
                    # Try to resolve function name, or use raw address
                    callee_info = r2.cmdj(f'afij @ {call_addr}')
                    if callee_info and isinstance(callee_info, list) and 'name' in callee_info[0]:
                        calls.append(callee_info[0]['name'])
                    else:
                        calls.append(f"sub_{call_addr:x}")

        results.append({
            'name':   func_name,
            'offset': func_offset,
            'size':   func_size,
            'n_args': nargs,
            'calls':  calls
        })

    r2.quit()
    return results


if __name__ == '__main__':
    match_pairs_list = []
    with open(path_file1, "rb") as f1, open(path_file2, "rb") as f2:
        first_data  = analyze_firmware(path_file1, base_addr_file1)
        second_data = analyze_firmware(path_file2, base_addr_file2)

        print(f"number of function in first file {len(first_data)}")
        print(f"number of function in second file {len(second_data)}")
        simThresh = 1.0
        while simThresh > 0.85:
            for func1 in first_data.copy():
                for func2 in second_data.copy():
                    if simThresh > 0.9:
                        if func1["n_args"] != func2["n_args"]:
                            continue
                        if len(func1["calls"]) != len(func2["calls"]):
                            continue
                    f1.seek(func1["offset"]-base_addr_file1)
                    f1_bytes = f1.read(func1["size"])
                    f2.seek(func2["offset"]-base_addr_file2)
                    f2_bytes = f2.read(func2["size"])
                    sim = bitwise_hamming_simmilarity(f1_bytes, f2_bytes)
                    if sim >= simThresh:
                        match_pairs_list.append((func1["name"], func2["name"], sim))
                        first_data.remove(func1)
                        second_data.remove(func2)
                        break
            simThresh -= 0.01
    print(f"\ncommon functions in files ({len(match_pairs_list)}):")
    for match in match_pairs_list:
        print("    "+str(match))
    print(f"\nfunctions only in first file ({len(first_data)}):")
    for func in first_data:
        print(f'    : {func["name"]}')
    print(f"\nfunctions only in first file ({len(second_data)}):")
    for func in second_data:
        print(f'    : {func["name"]}')
