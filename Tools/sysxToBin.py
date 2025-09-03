import numpy as np
from pathlib import Path
import crcmod
import sys

def extract_sysex_messages(syx_path):
    commands_list = dict([
        (0x71, "UPDATE_INIT"),
        (0x72, "UPDATE_WRITE"),
        (0x73, "UPDATE_FINISH"),
        (0x76, "UPDATE_FOOTER"),
        (0x7c, "UPDATE_HEADER"),
    ])
    
    def parse_nibble(data):    
        result = 0
        for byte_value in data:
            result = result << 4
            result |= byte_value
        return result

    with open(syx_path, 'rb') as syx_file:
        data = syx_file.read()

    finalFirmwareFile = np.empty([0],dtype=np.uint8)
    i = 0
    while i < len(data):
        if data[i] == 0xF0:  #SysEx start byte
            end_index = data.find(0xF7, i) #SysEx end byte
            if end_index == -1:
                raise ValueError("Missing SysEx end byte")
            novation_header = bytes([0x00, 0x20, 0x29, 0x00])
            if data[i+1:i+5] != novation_header:
                raise ValueError("File is missing novation header")
            command      = commands_list[data[i+5]]
            cropped_data = data[i+6:end_index]
            if command == "UPDATE_INIT":
                version = parse_nibble(cropped_data[2:8])
                print(f"init version: {version}")
            elif command == "UPDATE_HEADER":
                version  = parse_nibble(cropped_data[1:7])
                print(f"header version {version}")
                filesize = parse_nibble(cropped_data[7:15])
                print(f"header filesize {hex(filesize)}")
                checksum = parse_nibble(cropped_data[15:23])
                print(f"header checksum {hex(checksum)}")
            elif command in ["UPDATE_WRITE", "UPDATE_FINISH"]:
                #need to tightly pack 7bit MIDI bytes into 8bit firmware file
                packed   = np.frombuffer(cropped_data, dtype=np.uint8)
                unpacked = np.unpackbits(packed[:, np.newaxis], axis=1)
                unpacked = unpacked[:, 1:].reshape(-1) #discard first bit of each byte and make continuous array
                repacked = np.packbits(unpacked[:-3])  #last three bits are just padding
                if command == "UPDATE_FINISH":
                    finalFirmwareFile = np.concatenate([repacked, finalFirmwareFile])
                    break
                else:
                    finalFirmwareFile = np.concatenate([finalFirmwareFile, repacked])
            i = end_index + 1
        else:
            i += 1
    
    finalFirmwareFile   = bytes(finalFirmwareFile[:filesize])
    crc32_non_reflected = crcmod.mkCrcFun(0x104C11DB7, rev=False, initCrc=0xFFFFFFFF, xorOut=0x00000000)
    calculated_checksum = crc32_non_reflected(finalFirmwareFile) 
    if calculated_checksum != checksum:
        raise ValueError(f"File checksum {calculated_checksum} does not match header checksum {checksum}")
    with open(syx_path.with_suffix(".bin"), 'wb') as f:
        f.write(finalFirmwareFile)
        
if len(sys.argv)!=2:
    print("need to give a path to a .syx file")
extract_sysex_messages(Path(sys.argv[1]))