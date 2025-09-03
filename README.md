# Circuit Tracks Reverse Engineering

  

## Components

* Main Processor: <a  href="https://www.st.com/en/microcontrollers-microprocessors/stm32f745ve.html">STM32f745VEH6

* NOR Flash: MX25L25645G 256Mbit

* Audio Co-Processor: DSPB56725AG

  
| Chip                | Type                                                                                                                                             | Datasheet                                                                                                       | Location                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| STM32F 745VEH6      | ARM®-based Cortex®-M7 32b MCU+FPU, 462DMIPS, up to 1MB Flash/320+16+ 4KB<br>RAM, USB OTG HS/FS, ethernet, 18 TIMs, 3 ADCs, 25 com itf, cam & LCD | [Link](https://www.mouser.com/datasheet/2/389/stm32f745ie-1851206.pdf)                                          | Top of board, right near USB and Battery |
| DSPB56724AG         | Symphony™ DSP56724/ DSP56725 Multi-Core Audio Processors                                                                                         | [Link](https://www.mouser.com/datasheet/2/302/DSP56724EC-3138382.pdf)                                           | Under RF Shield, top of board            |
| MX25L25645G         | 3V, 256M-BIT [x 1/x 2/x 4] CMOS MXSMIO® (SERIAL MULTI I/O) FLASH MEMORY                                                                          | [Link](https://www.mxic.com.tw/Lists/Datasheet/Attachments/8906/MX25L25645G,%203V,%20256Mb,%20v2.0.pdf)         | Bottom side of board, bottom left        |
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

<image  src="./Documentation/Diagrams/debugHeader.svg">
<image  src="./Documentation/Mainboard-Photos/j3_debug_port.png">
