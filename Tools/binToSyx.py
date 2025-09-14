import numpy as np
from pathlib import Path
import crcmod
import sys

def pack_sysex_messages(firmwareFileData, firmwareVersion = 1394, targetDevice="tracks"):
    device_list = dict([
        ("tracks", 0x64),
        ("rhythm", 0x63),
    ])
    commands_list = dict([
        ("UPDATE_INIT", 0x71),
        ("UPDATE_WRITE", 0x72),
        ("UPDATE_FINISH", 0x73),
        ("UPDATE_FOOTER", 0x76),
        ("UPDATE_HEADER", 0x7c),
    ])
    
    def encode_nibble(data, numBytes):
        outputBytes = []
        mask = 0xf
        for byteIdx in range(numBytes):
            outputBytes.append((data & mask<<(byteIdx*4))>>(byteIdx*4))
        return outputBytes[::-1]

    
    finalSysexFile = bytes()
    #update init
    updateInit = bytes([0xF0, 0x00, 0x20, 0x29, 0x00,
                        commands_list["UPDATE_INIT"], 0x01,
                        device_list[targetDevice],  0x00, 0x00,
                        *encode_nibble(firmwareVersion, numBytes = 4),
                        0xF7])
    finalSysexFile += updateInit
    
    #update header
    #calculate firmware crc
    crc32_non_reflected = crcmod.mkCrcFun(0x104C11DB7, rev=False, initCrc=0xFFFFFFFF, xorOut=0x00000000)
    calculated_checksum = crc32_non_reflected(firmwareFileData) 
    updateHeader = bytes([0xF0, 0x00, 0x20, 0x29, 0x00,
                        commands_list["UPDATE_HEADER"], 0x00, 0x00, 0x00,
                        *encode_nibble(firmwareVersion,       numBytes = 4),
                        *encode_nibble(len(firmwareFileData), numBytes = 8),
                        *encode_nibble(calculated_checksum,   numBytes = 8),
                        0xF7])
    finalSysexFile += updateHeader
    
    bitsPerSysexPkg = 37*7 - 3 #is 256
    packed          = np.frombuffer(firmwareFileData, dtype=np.uint8)
    unpacked        = np.unpackbits(packed[:, np.newaxis], axis=1).reshape(-1)  #split into array of bits
    alignmentOffset = (bitsPerSysexPkg)-unpacked.size%(bitsPerSysexPkg)
    padding         = np.clip(alignmentOffset, 0, bitsPerSysexPkg - 1)
    unpacked        = np.pad(unpacked, (0,padding), constant_values=1)
    unpacked        = unpacked.reshape((-1, bitsPerSysexPkg))       #partition into syxex packets
    unpacked        = np.pad(unpacked, ((0,0),(0,3)))               #pad three bits on end of message
    unpacked        = unpacked.reshape((-1,37,7))                   #split into seven bit midi packets
    unpacked        = np.pad(unpacked, ((0,0),(0,0),(1,0)))         #pad first bit for midi
    unpacked        = unpacked.reshape((-1, 8*37))
    packed          = np.packbits(unpacked, axis = 1)
    
    for dataOffset in range(1, packed.shape[0]):
        #update write
        updateWrite  = bytes([0xF0, 0x00, 0x20, 0x29, 0x00, commands_list["UPDATE_WRITE"]])
        updateWrite += bytes(packed[dataOffset,:])
        updateWrite += bytes([0xF7])
        finalSysexFile += updateWrite
        
    #update finish
    updateFinish  = bytes([0xF0, 0x00, 0x20, 0x29, 0x00, commands_list["UPDATE_FINISH"]])
    updateFinish += bytes(packed[0,:])
    updateFinish += bytes([0xF7])
    finalSysexFile += updateFinish
    
    return finalSysexFile
    with open() as f:
        f.write(finalSysexFile)

if __name__ == "__main__":
    if len(sys.argv)!=2:
        print("need to give a path to a .bin file")
    bin_Path = Path(sys.argv[1])
    with open(bin_Path, 'rb') as inFile, open(bin_Path.with_suffix(".patched.syx"), 'wb') as outFile:
        firmwareFileData = inFile.read()
        outFile.write(pack_sysex_messages(firmwareFileData))
