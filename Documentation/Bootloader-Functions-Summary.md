# Circuit Tracks Bootloader - Known Functions Summary


## Bootloader Information
- **File**: dumpCT_flash_0x08000000.bin, first 0x10000 bytes
## Function Categories

### File System Operations
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x801855c | Memory_ReadInt32 | 0x16 | Read 32-bit integer from memory |
| 0x8018572 | Memory_WriteInt32 | 0x10 | Write 32-bit integer to memory |
| onlyF | memcmp_n | 0x18 | Memory comparison function |
| 0x801859a | FS_ValidateHeader | 0x44 | Validate filesystem header |
| 0x80185de | FS_ReadSector | 0x34 | Read filesystem sector |
| 0x8018612 | FS_InitializeBootSector | 0x86 | Initialize boot sector |
| 0x8018698 | FAT_ClusterToSector | 0x1a | Convert FAT cluster to sector |
| 0x80186b2 | FAT_GetNextCluster | 0xee | Get next cluster in FAT chain |
| 0x80187a0 | FAT_UpdateTableEntry | 0x140 | Update FAT table entry |
| 0x80188e0 | FAT_FreeClusterChain | 0x70 | Free cluster chain |
| 0x8018950 | FAT_AllocateCluster | 0x1be | Allocate new cluster |
| 0x8018b0e | FS_AdvanceDirectoryEntry | 0xbc | Advance directory entry |
| 0x8018bd6 | DirEntry_GetStartCluster | 0x1e | Get start cluster from directory entry |
| 0x8018bf4 | DirEntry_SetStartCluster | 0x18 | Set start cluster in directory entry |
| 0x8018c28 | VFAT_ProcessLongFilename | 0x12a | Process VFAT long filename |
| 0x8018d52 | FAT32_ScanDirectoryEntries | 0x446 | Scan FAT32 directory entries |
| 0x80196e8 | FS_GetFreeSlot | 0x4a | Get free filesystem slot |
| 0x8019734 | FS_CheckBootSector | 0x64 | Check boot sector validity |
| 0x80197a0 | FS_MountVolume | 0x2b2 | Mount filesystem volume |
| 0x8019ae4 | FS_OpenFile | 0x1e2 | Open file |
| 0x801a75c | FS_CheckDriveStatus | 0x2e | Check drive status |
| 0x801a78a | FS_GetDriveInfo | 0xc | Get drive information |
| 0x801a7ac | FS_WriteSector | 0x16 | Write filesystem sector |
| 0x801a7c2 | FS_FlushCache | 0x16 | Flush filesystem cache |

### Memory Management
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| onlyF | Memory_Clear | 0x6 | Clear memory region |
| 0x08001878 | Memory_Copy | 0x3e | Copy memory region |
| 0x08005018 | Memory_Allocate | 0x1a | Allocate memory |
| 0x080030f4 | Heap_Allocate | 0x2 | Heap allocation |
| onlyF | j_Memory_Allocate | 0x4 | Jump to memory allocate |
| onlyF | Memory_CopyBytes | 0x96 | Copy bytes between memory regions |
| onlyF | j_Memory_Set | 0x6 | Jump to memory set |

### Audio Processing
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x801aa14 | Audio_CopyBuffer | 0x20 | Copy audio buffer |
| 0x801e810 | Audio_InitializeBuffers | 0x84 | Initialize audio buffers |
| 0x801e8f0 | Audio_ProcessEventCallbacks | 0x66 | Process audio event callbacks |
| 0x801e956 | Audio_ProcessBufferEvents | 0x194 | Process audio buffer events |
| 0x8023698 | Audio_ProcessNoteEnvelope | 0xe4 | Process note envelope |
| 0x8023784 | AudioProcessor_InitializeWrapper | 0x2a | Audio processor init wrapper |
| 0x80237ae | AudioProcessor_Initialize | 0xb2 | Initialize audio processor |
| 0x8023868 | AudioProcessor_GetParameter | 0x1e | Get audio processor parameter |
| 0x8023540 | AudioBuffer_Initialize | 0x7a | Initialize audio buffer |
| 0x8024cdc | Audio_InitializeWithMagic | 0x40 | Initialize audio with magic number |
| 0x805011e | Audio_GetSampleRate | 0x10 | Get audio sample rate |
| 0x8050146 | Audio_CheckMute | 0x16 | Check audio mute status |
| 0x805015c | Audio_CheckSolo | 0x10 | Check audio solo status |
| 0x805016c | Audio_IsPlaying | 0x1c | Check if audio is playing |

### Hardware Control
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x080019b0 | Hardware_ConfigureChannels | 0x174 | Configure hardware channels |
| 0x08001b24 | Hardware_ProcessChannel | 0xe | Process hardware channel |
| 0x801b13e | Hardware_IsChannelReady | 0x16 | Check if channel is ready |
| 0x801bde8 | Hardware_ConditionalInit | 0x32 | Conditional hardware init |
| 0x801be1a | Hardware_Initialize | 0x46 | Initialize hardware |
| 0x801c072 | Hardware_ConfigureChannel | 0xd0 | Configure single hardware channel |
| 0x801c142 | Hardware_EnableDisplayChannel | 0xac | Enable display channel |
| 0x801c690 | Hardware_ProcessStatusFlags | 0xae | Process hardware status flags |
| 0x801e790 | Hardware_ProcessChannelArray | 0x22 | Process channel array |
| 0x801e7b2 | Hardware_GetChannelStatus | 0x50 | Get channel status |
| 0x801eeb0 | Hardware_ProcessInterrupt | 0xf8 | Process hardware interrupt |
| 0x80233de | Hardware_SetState | 0x36 | Set hardware state |
| 0x8023438 | Hardware_InitializeChannelSequence | 0x38 | Initialize channel sequence |
| 0x8025ae8 | Hardware_ProcessData | 0x28 | Process hardware data |

### MIDI Processing
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x0800700e | MIDI_SendToPort | 0x28 | Send MIDI to port |
| 0x8020c90 | MIDI_ProcessSysEx | 0x10a | Process MIDI SysEx messages |
| 0x8020ea0 | MIDI_ProcessInputLoop | 0xf0 | MIDI input processing loop |
| 0x8021e9c | MIDI_MapNoteToCategory | 0x12a | Map MIDI note to category |
| 0x8021fdc | MIDI_ProcessChannelEvent | 0xea | Process MIDI channel event |
| 0x08004d40 | MIDI_StartTransaction | 0x2a | Start MIDI transaction |
| 0x08004d6a | MIDI_SendData | 0x32 | Send MIDI data |
| 0x8024a10 | MIDI_ProcessMessage | 0xa6 | Process MIDI message |
| 0x8024ab6 | MIDI_SendBytes | 0x46 | Send MIDI bytes |
| 0x8024c80 | MIDI_BuildSysExMessage | 0x5c | Build MIDI SysEx message |
| 0x80268d6 | MIDI_SendToAllChannels | 0x22 | Send MIDI to all channels |
| 0x804d242 | MIDI_ProcessNoteEvent | 0x9e | Process MIDI note event |
| 0x804d504 | MIDI_ProcessNoteOff | 0x44 | Process MIDI note off |
| 0x8058380 | MIDI_TransmitWithStateMachine | 0x128 | MIDI transmit with state machine |
| 0x8058ecc | MIDI_ParseMessage | 0xba | Parse MIDI message |

### DSP Operations
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x801f4be | DSP_ProcessCallback | 0x36 | Process DSP callback |
| 0x801f554 | DSP_Upload | 0x72 | Upload to DSP |
| 0x802108c | DSP_Initialize | 0xa2 | Initialize DSP |
| 0x802112e | DSP_ConfigureChannel | 0x68 | Configure DSP channel |
| 0x8021196 | DSP_SetupAudio | 0x32 | Setup DSP audio |
| 0x8021246 | DSP_ApplySettings | 0x2c | Apply DSP settings |
| 0x8021272 | DSP_SetMode | 0x78 | Set DSP mode |
| 0x80212ea | DSP_ConfigureParameters | 0x86 | Configure DSP parameters |
| 0x8021370 | DSP_FinalizeInit | 0x22 | Finalize DSP initialization |
| 0x80217b4 | DSP_GetTimestamp | 0x1c6 | Get DSP timestamp |
| 0x80219e8 | DSP_UpdateParameters | 0x260 | Update DSP parameters |
| 0x8021d86 | DSP_ConfigureAudioParams | 0x4a | Configure DSP audio parameters |
| 0x8021dd4 | DSP_ConfigureAudioParamsDefault | 0x4 | Configure default DSP audio params |
| 0x8021dd8 | DSP_ProcessVoiceStates | 0xbe | Process DSP voice states |
| 0x80220f4 | j_DSP_ConfigureAllModules | 0x4 | Configure all DSP modules |
| 0x80220fc | j_DSP_ConfigureModule33 | 0x4 | Configure DSP module 33 |
| onlyF | DSP_InitializeAudioSystem | 0x6a | Initialize DSP audio system |

### System Control
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x08001c44 | SysTick_Initialize | 0x26 | Initialize system tick |
| 0x08001c6a | SysTick_SetClockSource | 0x1a | Set system tick clock source |
| ? | System_InitializeProcessor | 0x3c | Initialize system processor |
| 0x08004f38 | Clock_GetSystemFrequency | 0x6a | Get system clock frequency |
| ? | System_MainLoop | 0x1d0 | Main system loop |
| ? | System_InitializeObjects | 0xde | Initialize system objects |
| onlyF | System_InitSubsystems | 0x160 | Initialize subsystems |
| onlyF | System_InitializeComponents | 0x142 | Initialize system components |
| onlyF | System_MasterInitialization | 0x131e | Master system initialization |
| onlyF | System_SetPowerState | 0x5a | Set system power state |
| ? | System_SetGlobalReference | 0x6 | Set global system reference |
| ? | System_Initialize | 0xa | System initialization |
| ? | System_InitializeExtended | 0xa | Extended system initialization |
| ? | System_ConditionalInit | 0x18 | Conditional system initialization |
| onlyF | MainLoop_SystemManager | 0x3e | Main loop system manager |

### Display Control
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x08003e30 | Display_ProcessMatrix | 0x90 | Process display matrix |
| onlyF | Display_SetLED | 0xe | Set LED state |
| onlyF | Display_UpdateFromLookup | 0x3e | Update display from lookup table |
| onlyF | Display_Initialize8Elements | 0x68 | Initialize 8 display elements |
| ? | Display_UpdateConditional | 0x5a | Conditional display update |

### Sequencer Operations
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| onlyF | Sequencer_ProcessEvents | 0xdc | Process sequencer events |
| ? | Sequencer_ProcessAllTracks | 0x100 | Process all sequencer tracks |
| onlyF | Sequencer_UpdateDisplay | 0x4e | Update sequencer display |
| onlyF | Sequencer_Process32Steps | 0xa8 | Process 32 sequencer steps |

### Track Management
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| onlyF | DrumTrack_IsEnabled | 0x28 | Check if drum track is enabled |
| onlyF | DrumTrack_SetNote | 0x30 | Set drum track note |
| onlyF | DrumTrack_TriggerNote | 0x1a | Trigger drum track note |
| onlyF | DrumTrack_AddEvent | 0xe0 | Add drum track event |
| ? | DrumTrack_ProcessEvents | 0x3fc | Process drum track events |
| onlyF | SynthTrack_ProcessEvents | 0x108 | Process synth track events |
| onlyF | Track_SelectWithValidation | 0x28 | Select track with validation |
| onlyF | Track_UpdateDisplay | 0x38 | Update track display |
| ? | DrumTrack_ProcessStep | 0xf4 | Process drum track step |
| onlyF | DrumTrack_ClearStep | 0x62 | Clear drum track step |
| ? | DrumTrack_SetStep | 0xbe | Set drum track step |
| onlyF | DrumTrack_WriteStepWithVelocity | 0x50 | Write drum step with velocity |
| onlyF | Track_HandleTrigger | 0x186 | Handle track trigger |
| onlyF | Track_HandleRelease | 0x88 | Handle track release |
| ? | Track_HandleEvents | 0x110 | Handle track events |
| onlyF | Track_ProcessTrigger | 0xb6 | Process track trigger |
| ? | Track_UpdateState | 0x62 | Update track state |
| onlyF | Track_ProcessMute | 0x66 | Process track mute |
| onlyF | Track_SetParameter | 0x1e | Set track parameter |
| onlyF | Track_UpdateLED | 0xb2 | Update track LED |
| onlyF | Track_GetBufferByType | 0x36 | Get track buffer by type |
| onlyF | Track_SetType1AndClear | 0x22 | Set track type 1 and clear |

### Interrupt Handlers
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| onlyF | PowerButton_IRQHandler | 0x4a | Power button interrupt handler |
| ? | PendSV_handler | 0x5c | PendSV interrupt handler |
| ? | SVCall_handler | 0x1c | SVC interrupt handler |
| 0x080051c6 | IRQ_ProcessTimer | 0x62 | Timer interrupt processor |
| onlyF | Timer_IRQ15_Handler | 0x2a | Timer 15 interrupt handler |
| onlyF | Timer_IRQ14_Handler | 0x30 | Timer 14 interrupt handler |
| 0x805995e | NMI_handler | 0x2 | NMI interrupt handler |
| 0x8059960 | HardFault_handler | 0x2 | Hard fault handler |
| 0x8059962 | MemManage_fault_handler | 0x2 | Memory management fault handler |
| 0x8059964 | BusFault_handler | 0x10 | Bus fault handler |
| 0x8059978 | UsageFault_handler | 0x10 | Usage fault handler |
| 0x805998a | DebugMonitor_handler | 0x2 | Debug monitor handler |
| 0x08009330 | SysTick_Handler | 0x10 | System tick handler |
| 0x0800935c | SysTick_UpdateCounter | 0xc | Update system tick counter |
| ? | Reset_handler | 0x19c | System reset handler |

### GPIO and Pin Control
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x08006378 | GPIO_ConfigurePin | 0x1c2 | Configure GPIO pin |
| ? | GPIO_EnablePortClock | 0x82 | Enable GPIO port clock |
| 0x080066b6 | GPIO_SetAlternateFunction | 0x80 | Set GPIO alternate function |

### Timer Operations
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| ? | Timer_InitializeHardware | 0xa8 | Initialize timer hardware |

### Utility Functions
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| onlyF | String_ParseNumericID | 0x5a | Parse numeric ID from string |
| 0x08005d0c | String_Compare | 0x68 | Compare strings |
| onlyF | String_Search | 0x154 | Search within string |
| onlyF | Math_FloatMultiply | 0x1a2 | Floating point multiplication |
| onlyF | Control_GetBootMode | 0x26 | Get boot mode control |
| 0x08003dac | Buffer_ClearWithFF | 0xc | Clear buffer with 0xFF |
| onlyF | Buffer_Initialize | 0x12 | Initialize buffer |
| 0x080084ce | Buffer_GetPointer | 0x22 | Get buffer pointer |
| onlyF | Component_InitializeWithCallback | 0x32 | Initialize component with callback |
