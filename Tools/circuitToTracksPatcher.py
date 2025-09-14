from pathlib import Path
import syxToBin
import binToSyx

syx_path = Path.cwd()/"circuitrhythm-firmware-5706.syx"
with open(syx_path, 'rb') as inFile, open(syx_path.with_suffix(".patch_ct2cr.syx"), 'wb') as outFile:
    firmwareData, fwVer, devName = syxToBin.extract_sysex_messages(inFile.read())
    firmwareData = bytearray(firmwareData)
    #patching code
    print(firmwareData[0x1cd])
    firmwareData[0x1cd] = 0x64
    devName = "tracks"
    
    modifiedSyx = binToSyx.pack_sysex_messages(firmwareData, fwVer, devName)
    outFile.write(modifiedSyx)