def init_sram_bssSections(bootloaderBinary, sramInstructionPos):
    while True:
        size = readUint32FromFlash(sramInstructionPos)
        sramInstructionPos += 4
        startAdd = readUint32FromFlash(sramInstructionPos)
        sramInstructionPos += 4
        for offset in range(size):
            writeUint8FromSram(startAdd+offset, 0x00)
        if readUint32FromFlash(sramInstructionPos) == 0:
            return

def init_sram_dataSections(bootloaderBinary, sramInstructionPos):
    currentSramInstructionPos = sramInstructionPos
    flash_offset = readUint32FromFlash(currentSramInstructionPos)
    currentSramInstructionPos += 4
    size_and_flags = readUint32FromFlash(currentSramInstructionPos)
    currentSramInstructionPos += 4
    sram_dest_offset = readUint32FromFlash(currentSramInstructionPos)
    currentSramInstructionPos += 4


    compressed_flag   = size_and_flags & 0x1
    size_bytes        = size_and_flags >> 1
    use_extra_offset  = (size_and_flags >> 31) & 0x1

    # Calculate source and destination pointers
    src = sramInstructionPos + flash_offset         # r3 = r2 + [r2]
    dest = sram_dest_offset                      # r5 = [r2 + 8]

    if use_extra_offset:
        dest += extra_offset                     # r5 += param_3

    end = src + (size_bytes >> 1)                # r4 = r3 + (size >> 1)
    while src < end:
        header = readUint8FromFlash(src)
        src += 1

        copy_count = header & 0x3
        if copy_count == 0:                 #larger copy
            copy_count = readUint8FromFlash(src) + 3
            src += 1

        backcopy_count = header >> 4
        if backcopy_count == 0xF:
            backcopy_count = readUint8FromFlash(src) + 0xF
            src += 1

        # Copy from flash to SRAM
        for _ in range(copy_count-1):
            writeUint8FromSram(dest, readUint8FromFlash(src))
            dest += 1
            src += 1


        if backcopy_count != 0:
            low = readUint8FromFlash(src)
            src += 1
            header_bits_2_3 = (header >> 2) & 0x3
            if header_bits_2_3 == 3:
                high = readUint8FromFlash(src)
                src += 1
            else:
                high = header_bits_2_3
            offset = (high << 8) | low

            back_src = dest - offset

            for _ in range(backcopy_count + 2):
                writeUint8FromSram(dest, readUint8FromSram(back_src))
                dest += 1
                back_src += 1

offsetFlash = 0x08000000
offsetRam = 0x20000000
sram = bytearray([0xFF] * 320 * 1024)

def writeUint8FromSram(address, byte):
    print(f"write sram {hex(address)}, {hex(byte)}")
    sram[address-offsetRam] = byte
def readUint8FromSram(address):
    return sram[address-offsetRam]
def readUint32FromFlash(address):
    readAddr = address-offsetFlash
    data = bootloaderBinary[readAddr: readAddr+4]
    data = int.from_bytes(data, byteorder='little')
    return data
def readUint8FromFlash(address):
    readAddr = address-offsetFlash
    return bootloaderBinary[readAddr]


with open("dumpCT_flash_0x08000000.bin", "rb") as bootloaderFlash:
    bootloaderBinary = bootloaderFlash.read()
    init_sram_bssSections(bootloaderBinary,  0x0800967c)
    init_sram_dataSections(bootloaderBinary, 0x08009694)

with open("ram_before_main.bin", "wb") as sramImage:
    sramImage.write(sram)