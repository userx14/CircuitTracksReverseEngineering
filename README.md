# Circuit Tracks Reverse Engineering
## Components
| Chip                | Type                                                                                                                                             | Datasheet                                                                                                       | Location                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| STM32F745VEH6       | ARM®-based Cortex®-M7 32b MCU+FPU, 462DMIPS, 512KB Flash / 320KB SRAM, USB OTG HS/FS, ethernet, 18 TIMs, 3 ADCs, 25 com itf, cam & LCD | [Link](https://www.st.com/resource/en/datasheet/stm32f745ve.pdf)                                          | Top of board, right near USB and Battery |
| DSPB56724AG         | Symphony™ DSP56724/ DSP56725 Multi-Core Audio Processors                                                                                         | [Link](https://www.mouser.com/datasheet/2/302/DSP56724EC-3138382.pdf)                                           | Under RF Shield, top of board            |
| MX25L25645G         | NOR Flash, 256M-BIT, 3V, [x 1/x 2/x 4] CMOS MXSMIO® (SERIAL MULTI I/O) FLASH MEMORY                                                                          | [Link](https://www.mxic.com.tw/Lists/Datasheet/Attachments/8906/MX25L25645G,%203V,%20256Mb,%20v2.0.pdf)         | Bottom side of board, bottom left        |
| IS42S16160G-7TLI-TR | 32Meg x 8, 16Meg x16 256Mb SYNCHRONOUS DRAM                                                                                                      | [Link](https://www.mouser.com/datasheet/2/198/42_45S83200G_16160G-258274.pdf)                                   | Under RF Shield, top of board            |
| LVT573              | Low Voltage Octal Transparent Latch with 3-STATE Outputs                                                                                         | [Link](https://www.mouser.com/datasheet/2/149/74lvt573-289200.pdf)                                              | Under RF Shield, top of board            |
| MPSM36 MP2633       | Switching Charger for Battery                                                                                                                    | [Link](https://www.monolithicpower.com/en/mp2633.html)                                                          |                                          |
| 74HC4051D           | Nexperia 8 channel analog multiplexer/demultiplexer                                                                                              | [Link](https://assets.nexperia.com/documents/data-sheet/74HC_HCT4051.pdf)                                       |                                          |
| 2746J32 JRC         | Single supply, rail to rail dual op-amp                                                                                                          | [Link](https://www.nisshinbo-microdevices.co.jp/en/pdf/datasheet/NJM2746_E.pdf)                                 | Bloody everywhere                        |
| AKM 4556VT          | 3V 192kHz 24Bit Stereo Delta Sigma Codec                                                                                                         | [Link](https://www.akm.com/content/dam/documents/products/audio/audio-codec/ak4556vt/ak4556vt-en-datasheet.pdf) |                                          |

### LiPo battery

* BAKTH LP-306987-1S-3, 3.7 V

* 4 × 70 × 90 mm, 44 g

* 2200 mAh, 8.14 Wh

* 10kOhm Thermistor (yellow to black)

* cut off voltage: 2.8 V

  

## Debugging header
10-Pin Legged TC2050 Plug-of-Nails™ programming cable would be compatible.

<image  src="./Documentation/Diagrams/debugHeader.svg">
<image  src="./Documentation/Mainboard-Photos/j3_debug_port.png">
