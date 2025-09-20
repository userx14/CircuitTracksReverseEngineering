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

## Microcontroller pinout
| **Pin** | **Function**         |
|--------|----------------------|
| **UART** |
| PA9    | UART1_TX            |
| PB7    | UART1_RX            |
| PD5    | UART2_TX            |
|        |                      |
| **SPI2** |
| PC1    | SPI2_MOSI           |
| PC2    | SPI2_MISO           |
| PD3    | SPI2_SCK            |
|        |                      |
| **SPI4** |
| PE14   | SPI4_MOSI           |
| PE13   | SPI4_MISO           |
| PE12   | SPI4_SCK            |
|        |                      |
| **SDMMC1** |
| PD2    | SDMMC1_CMD          |
| PC8    | SDMMC1_D0           |
| PC9    | SDMMC1_D1           |
| PC10   | SDMMC1_D2           |
| PC11   | SDMMC1_D3           |
| PC12   | SDMMC1_CK           |
|        |                      |
| **QUADSPI** |
| PB2    | QUADSPI_CLK         |
| PD11   | QUADSPI_BK1_IO0     |
| PD12   | QUADSPI_BK1_IO1     |
| PE2    | QUADSPI_BK1_IO2     |
| PD13   | QUADSPI_BK1_IO3     |
| PB6    | QUADSPI_BK1_NCS     |
|        |                      |
| **Clock Output** |
| PA8    | MCO1                |
|        |                      |
| **USB OTG HS** |
| PB14   | USB_OTG_HS_DM       |
| PB15   | USB_OTG_HS_DP       |
|        |                      |
| **Outputs** |
| PA12   | Output              |
| PB1    | Output              |
| PB4    | Output              |
| PB8    | Output              |
| PB9    | Output              |
| PB10   | Output              |
| PB11   | Output              |
| PB12   | Output              |
| PC0    | Output              |
| PC4    | Output              |
| PC6    | Output              |
| PC15   | Output              |
| PD0    | Output              |
| PD1    | Output              |
| PD6    | Output              |
| PD8    | Output              |
| PD9    | Output              |
| PE3    | Output              |
| PE4    | Output              |
| PE10   | Output (Speed 2)    |
| PE11   | Output              |
| PE15   | Output              |
|        |                      |
| **Inputs** |
| PA10   | Input               |
| PA11   | Input (Speed 1)     |
| PA15   | Input               |
| PC5    | Input (Pull-Up)     |
| PC7    | Input               |
| PD4    | Input               |
| PD7    | Input               |
| PD10   | Input               |
| PD14   | Input               |
| PD15   | Input               |
| PE0    | Input               |
| PE2    | Input (Speed 1)     |
| PE7    | Input (Speed 1)     |
| PE8    | Input (Speed 1)     |
| PE9    | Input (Speed 1)     |
|        |                      |
| **Analog Inputs** |
| PA0    | Analog0             |
| PA1    | Analog1             |
| PA2    | Analog2             |
| PA3    | Analog3             |
| PA4    | Analog4             |
| PA5    | Analog5             |
| PA6    | Analog6             |

