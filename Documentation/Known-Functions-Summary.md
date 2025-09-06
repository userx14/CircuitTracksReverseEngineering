# Circuit Tracks Firmware - Known Functions Summary

This document provides a summary of the identified and analyzed functions in the Circuit Tracks firmware (version 4486) based on IDA Pro analysis. The functions are based on `0x8010000` because the bootloader is missing from the dump I did not get a chance to use the full flash dump with bootloader included yet. Most of this is AI generated as this was a very nice opportunity to learn how to use IDA Pro and AI together in the spirit of https://wilgibbs.com/blog/defcon-finals-mcp/ so take everything with a grain of salt.

## Firmware Information
- **File**: circuittracks-firmware-4486.bin

## Function Categories

### File System Operations
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x801855c | Memory_ReadInt32 | 0x16 | Read 32-bit integer from memory |
| 0x8018572 | Memory_WriteInt32 | 0x10 | Write 32-bit integer to memory |
| 0x8018582 | memcmp_n | 0x18 | Memory comparison function |
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
| 0x801a7e4 | Memory_Clear | 0x6 | Clear memory region |
| 0x801aa34 | Memory_Copy | 0x3e | Copy memory region |
| 0x801cfa4 | Memory_Allocate | 0x1a | Allocate memory |
| 0x801d7d0 | Heap_Allocate | 0x2 | Heap allocation |
| 0x801d808 | j_Memory_Allocate | 0x4 | Jump to memory allocate |
| 0x801d8ac | Memory_CopyBytes | 0x96 | Copy bytes between memory regions |
| 0x801bc58 | j_Memory_Set | 0x6 | Jump to memory set |

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
| 0x801afbc | Hardware_ConfigureChannels | 0x174 | Configure hardware channels |
| 0x801b130 | Hardware_ProcessChannel | 0xe | Process hardware channel |
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
| 0x801c894 | MIDI_SendToPort | 0x28 | Send MIDI to port |
| 0x8020c90 | MIDI_ProcessSysEx | 0x10a | Process MIDI SysEx messages |
| 0x8020ea0 | MIDI_ProcessInputLoop | 0xf0 | MIDI input processing loop |
| 0x8021e9c | MIDI_MapNoteToCategory | 0x12a | Map MIDI note to category |
| 0x8021fdc | MIDI_ProcessChannelEvent | 0xea | Process MIDI channel event |
| 0x80224a8 | MIDI_StartTransaction | 0x2a | Start MIDI transaction |
| 0x80224d2 | MIDI_SendData | 0x32 | Send MIDI data |
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
| 0x80245c6 | DSP_InitializeAudioSystem | 0x6a | Initialize DSP audio system |

### System Control
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x801bbf8 | SysTick_Initialize | 0x26 | Initialize system tick |
| 0x801bc1e | SysTick_SetClockSource | 0x1a | Set system tick clock source |
| 0x801bc78 | System_InitializeProcessor | 0x3c | Initialize system processor |
| 0x801bcb4 | Clock_GetSystemFrequency | 0x6a | Get system clock frequency |
| 0x801d4b0 | System_MainLoop | 0x1d0 | Main system loop |
| 0x801df10 | System_InitializeObjects | 0xde | Initialize system objects |
| 0x801e174 | System_InitSubsystems | 0x160 | Initialize subsystems |
| 0x801ec80 | System_InitializeComponents | 0x142 | Initialize system components |
| 0x801f61c | System_MasterInitialization | 0x131e | Master system initialization |
| 0x8024794 | System_SetPowerState | 0x5a | Set system power state |
| 0x8025a1a | System_SetGlobalReference | 0x6 | Set global system reference |
| 0x8057650 | System_Initialize | 0xa | System initialization |
| 0x805765a | System_InitializeExtended | 0xa | Extended system initialization |
| 0x8057664 | System_ConditionalInit | 0x18 | Conditional system initialization |
| 0x805767c | MainLoop_SystemManager | 0x3e | Main loop system manager |

### Display Control
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x8020a5c | Display_ProcessMatrix | 0x90 | Process display matrix |
| 0x804aa40 | Display_SetLED | 0xe | Set LED state |
| 0x804fac0 | Display_UpdateFromLookup | 0x3e | Update display from lookup table |
| 0x8052580 | Display_Initialize8Elements | 0x68 | Initialize 8 display elements |
| 0x805260a | Display_UpdateConditional | 0x5a | Conditional display update |

### Sequencer Operations
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x80235ba | Sequencer_ProcessEvents | 0xdc | Process sequencer events |
| 0x804c16a | Sequencer_ProcessAllTracks | 0x100 | Process all sequencer tracks |
| 0x804c26a | Sequencer_UpdateDisplay | 0x4e | Update sequencer display |
| 0x804f5bc | Sequencer_Process32Steps | 0xa8 | Process 32 sequencer steps |

### Track Management
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x804ad50 | DrumTrack_IsEnabled | 0x28 | Check if drum track is enabled |
| 0x804ae66 | DrumTrack_SetNote | 0x30 | Set drum track note |
| 0x804b07a | DrumTrack_TriggerNote | 0x1a | Trigger drum track note |
| 0x804b094 | DrumTrack_AddEvent | 0xe0 | Add drum track event |
| 0x804b270 | DrumTrack_ProcessEvents | 0x3fc | Process drum track events |
| 0x804c062 | SynthTrack_ProcessEvents | 0x108 | Process synth track events |
| 0x804d59a | Track_SelectWithValidation | 0x28 | Select track with validation |
| 0x804d5ca | Track_UpdateDisplay | 0x38 | Update track display |
| 0x804f036 | DrumTrack_ProcessStep | 0xf4 | Process drum track step |
| 0x804f18c | DrumTrack_ClearStep | 0x62 | Clear drum track step |
| 0x804f262 | DrumTrack_SetStep | 0xbe | Set drum track step |
| 0x8050062 | DrumTrack_WriteStepWithVelocity | 0x50 | Write drum step with velocity |
| 0x8050ee8 | Track_HandleTrigger | 0x186 | Handle track trigger |
| 0x805106e | Track_HandleRelease | 0x88 | Handle track release |
| 0x80510f6 | Track_HandleEvents | 0x110 | Handle track events |
| 0x8051206 | Track_ProcessTrigger | 0xb6 | Process track trigger |
| 0x80512bc | Track_UpdateState | 0x62 | Update track state |
| 0x805131e | Track_ProcessMute | 0x66 | Process track mute |
| 0x8051384 | Track_SetParameter | 0x1e | Set track parameter |
| 0x80513a2 | Track_UpdateLED | 0xb2 | Update track LED |
| 0x80514ea | Track_GetBufferByType | 0x36 | Get track buffer by type |
| 0x805271a | Track_SetType1AndClear | 0x22 | Set track type 1 and clear |

### Interrupt Handlers
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x801da24 | PowerButton_IRQHandler | 0x4a | Power button interrupt handler |
| 0x801d954 | PendSV_handler | 0x5c | PendSV interrupt handler |
| 0x801d9b0 | SVCall_handler | 0x1c | SVC interrupt handler |
| 0x8022826 | IRQ_ProcessTimer | 0x62 | Timer interrupt processor |
| 0x8057508 | Timer_IRQ15_Handler | 0x2a | Timer 15 interrupt handler |
| 0x8057532 | Timer_IRQ14_Handler | 0x30 | Timer 14 interrupt handler |
| 0x805995e | NMI_handler | 0x2 | NMI interrupt handler |
| 0x8059960 | HardFault_handler | 0x2 | Hard fault handler |
| 0x8059962 | MemManage_fault_handler | 0x2 | Memory management fault handler |
| 0x8059964 | BusFault_handler | 0x10 | Bus fault handler |
| 0x8059978 | UsageFault_handler | 0x10 | Usage fault handler |
| 0x805998a | DebugMonitor_handler | 0x2 | Debug monitor handler |
| 0x805998c | SysTick_Handler | 0x10 | System tick handler |
| 0x80599b8 | SysTick_UpdateCounter | 0xc | Update system tick counter |
| 0x805c00c | Reset_handler | 0x19c | System reset handler |

### GPIO and Pin Control
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x801beb0 | GPIO_ConfigurePin | 0x1c2 | Configure GPIO pin |
| 0x801c1ee | GPIO_EnablePortClock | 0x82 | Enable GPIO port clock |
| 0x801c270 | GPIO_SetAlternateFunction | 0x80 | Set GPIO alternate function |

### Timer Operations
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x8022260 | Timer_InitializeHardware | 0xa8 | Initialize timer hardware |

### Utility Functions
| Address | Function Name | Size | Description |
|---------|---------------|------|-------------|
| 0x801f1c0 | String_ParseNumericID | 0x5a | Parse numeric ID from string |
| 0x8025180 | String_Compare | 0x68 | Compare strings |
| 0x8057e4c | String_Search | 0x154 | Search within string |
| 0x8051cd0 | Math_FloatMultiply | 0x1a2 | Floating point multiplication |
| 0x8020944 | Control_GetBootMode | 0x26 | Get boot mode control |
| 0x80209d8 | Buffer_ClearWithFF | 0xc | Clear buffer with 0xFF |
| 0x8024c18 | Buffer_Initialize | 0x12 | Initialize buffer |
| 0x8024808 | Buffer_GetPointer | 0x22 | Get buffer pointer |
| 0x8050188 | Component_InitializeWithCallback | 0x32 | Initialize component with callback |
