#load the binary firmware file
r2 -a arm -b 16 -m 0x08000000 dumpCT_flash_0x08000000.bin'

# analysis results
```
0x080098c8 -> reset vector
    0x08004ef9 -> enable coprocessor, enable clocks, set vector table offset 0x08000000
    0x0800990c -> second called function
        0x08009654 -> enable access to fpu
        0x080096dc
            0x08009608 ->
                    -> 0x080096a4
                        -> 0x080096c4 checks if args
            0x08002fb0 -> print bootloader start
                0x080031e0
                    0x08004abc -> enable debug, watchdog
                    0x08004ae2 -> refresh watchdog
                    0x08003262
                        0x080019b0 -> gpio init
                        0x08001b24
                        0x08004af4 -> something with external interrupts EXTI
                        0x08004b00 -> something with external interrupts EXTI
                        0x08004b0e -> something with external interrupts EXTI
                        0x08004afc -> something with external interrupts EXTI
                        0x08001b32 -> checks some bits in a mask
                    0x0800329a -> refers again to 0x08004af4, 4b00, 4afc,
                        0x8004b2c -> read RCC, RTC & BKP Registers, PWR
                            0x08004c58 -> RTC & BKP Register
                            0x08001bb6 -> AIRCR, NVIC_IPR0, SHPR1
                    0x08003326
                        0x08004ebc
                        0x08004ee0
                        0x08004cc6

                0x08003410
                0x080035fc

                0x08003628
                0x08003630
                0x08003704
                0x0800388a
                0x08003940
                0x080036b6
                    0x080027e4 -> "idle?"

            0x080096fa -> calls underlying function in loop
                0x08008b90 -> breakpoint, trigger exception
```
