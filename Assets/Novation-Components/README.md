## Reversing the wasm blob

The web version of novation components uses the wasm blob for validation of the ncs files before uploading them to the device

https://components.novationmusic.com/vendor/circuit-tracks-project-validator-e83caa525f3f586024af78cebcb33ad4.wasm

We need two things `ghidra` and a plugin for wasm dissasembly **[ghidra-wasm-plugin](https://github.com/nneonneo/ghidra-wasm-plugin)**

Just looking for the defined strings we are definitely at the right place to understand more about the structure of the file since the strings include stuff like  `--- Success Log : ---`, `--- Error Log : ---`, `VALIDATION LOG FOR SESSION FILE @`, `Session colour out of range`, `Tempo out of range`, `Scene pattern chain padding not set to 0`, ` has an invalid drum choice value`

This is a piece of code that is validating the `ncs` format, we can try to infer how `ncs` looks by checking how this code works 

## Finding entrypoint

We look for exported function and eyeball their decompilation output in ghidra eventually we find a function matching what ncs validator should be doing in  the exports, we traverse the function call tree until we find a function at `ram:8002e426` (renamed to `ncs_validation_orchestrator`) which very much looks like its running some validators over the ncs file in sequence, after some renaming it looks like this

```C

void run_validators(undefined4 param1,undefined4 *param2)

{
  int *piVar1;
  undefined4 *puVar2;
  int *piVar3;
  int iVar4;
  uint uVar5;
  undefined4 *puVar6;
  undefined4 *puVar7;
  undefined1 auStack_27430 [160816];
  
  uVar5 = (int)DAT_ram_00008594._4_4_ - (int)(int *)DAT_ram_00008594 >> 2;
  if (uVar5 < 0x81) {
    unnamed_function_257(&DAT_ram_00008594,0x81 - uVar5);
code_r0x8002e4ba:
    piVar1 = DAT_ram_00008594._4_4_;
    if (DAT_ram_00008594._4_4_ != (int *)DAT_ram_00008594) goto code_r0x8002e4c2;
  }
  else {
    if ((int)DAT_ram_00008594._4_4_ - (int)(int *)DAT_ram_00008594 == 0x204) goto code_r0x8002e4ba;
    DAT_ram_00008594._4_4_ = (int *)DAT_ram_00008594 + 0x81;
code_r0x8002e4c2:
    piVar1 = DAT_ram_00008594._4_4_;
    iVar4 = 0;
    piVar3 = (int *)DAT_ram_00008594;
    do {
      *piVar3 = iVar4;
      iVar4 = iVar4 + 1;
      piVar3 = piVar3 + 1;
    } while (piVar3 != piVar1);
  }
  piVar1[-1] = 0xff;
  uVar5 = (int)DAT_ram_000085a0._4_4_ - (int)(int *)DAT_ram_000085a0 >> 2;
  if (uVar5 < 0x41) {
    unnamed_function_257(&DAT_ram_000085a0,0x41 - uVar5);
code_r0x8002e551:
    piVar1 = DAT_ram_000085a0._4_4_;
    if (DAT_ram_000085a0._4_4_ == (int *)DAT_ram_000085a0) goto code_r0x8002e57b;
  }
  else {
    if ((int)DAT_ram_000085a0._4_4_ - (int)(int *)DAT_ram_000085a0 == 0x104) goto code_r0x8002e551;
    DAT_ram_000085a0._4_4_ = (int *)DAT_ram_000085a0 + 0x41;
  }
  piVar1 = DAT_ram_000085a0._4_4_;
  iVar4 = 0;
  piVar3 = (int *)DAT_ram_000085a0;
  do {
    *piVar3 = iVar4;
    iVar4 = iVar4 + 1;
    piVar3 = piVar3 + 1;
  } while (piVar3 != piVar1);
code_r0x8002e57b:
  piVar1[-1] = 0xff;
  iVar4 = memcpy(auStack_27430,*param2,&DAT_ram_0002740c);
  validate_header_and_feature_flags(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_timing_section(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_scenes_table(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_scene_chain_bounds_and_padding(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4)
  ;
  validate_pattern_chain_table(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_synth_patterns_chunkA(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_synth_patterns_chunkB(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_synth_patterns_chunkC(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_synth_patterns_chunkD(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_synth_patterns_chunkE(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_synth_track_info_table(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_drum_patterns_chunkA(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_drum_patterns_chunkB(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_drum_patterns_chunkC(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_drum_patterns_chunkD(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_drum_patterns_chunkE(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_drum_mute_state_table(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_default_drum_choices(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_midi_patterns_chunkA(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_midi_patterns_chunkB(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_midi_patterns_chunkC(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_midi_patterns_chunkD(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_midi_patterns_chunkE(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_midi_track_info_table(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_scale_settings(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_fx_presets(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_midi_keyboard_octaves(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  report_label_actualValue_helperA(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  report_label_actualValue_helperB(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  report_label_actualValue_helperC(iVar4,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  validate_root_orchestrator_stub(param1,&DAT_ram_00027420 + iVar4,&DAT_ram_00027410 + iVar4);
  puVar6 = *(undefined4 **)(&DAT_ram_00027410 + iVar4);
  if (puVar6 != (undefined4 *)0x0) {
    puVar2 = *(undefined4 **)(&DAT_ram_00027414 + iVar4);
    puVar7 = puVar6;
    if (puVar6 != *(undefined4 **)(&DAT_ram_00027414 + iVar4)) {
      do {
        if (*(char *)((int)puVar2 + -9) < '\0') {
          free(puVar2[-5]);
        }
        puVar7 = puVar2 + -8;
        if (*(char *)((int)puVar2 + -0x15) < '\0') {
          free(*puVar7);
        }
        puVar2 = puVar7;
      } while (puVar6 != puVar7);
      puVar7 = *(undefined4 **)(&DAT_ram_00027410 + iVar4);
    }
    *(undefined4 **)(&DAT_ram_00027414 + iVar4) = puVar6;
    free(puVar7);
  }
  puVar6 = *(undefined4 **)(&DAT_ram_00027420 + iVar4);
  if (puVar6 != (undefined4 *)0x0) {
    puVar2 = *(undefined4 **)(&DAT_ram_00027424 + iVar4);
    puVar7 = puVar6;
    if (puVar6 != *(undefined4 **)(&DAT_ram_00027424 + iVar4)) {
      do {
        if (*(char *)((int)puVar2 + -9) < '\0') {
          free(puVar2[-5]);
        }
        puVar7 = puVar2 + -8;
        if (*(char *)((int)puVar2 + -0x15) < '\0') {
          free(*puVar7);
        }
        puVar2 = puVar7;
      } while (puVar6 != puVar7);
      puVar7 = *(undefined4 **)(&DAT_ram_00027420 + iVar4);
    }
    *(undefined4 **)(&DAT_ram_00027424 + iVar4) = puVar6;
    free(puVar7);
  }
  return;
}


```



## Function Address Map

Based on Ghidra analysis of the WASM blob, here are the key function addresses:

### Main Orchestrator Functions
- `ncs_validation_orchestrator` @ `ram:8002e426` - Main validation orchestrator that calls all validators
- `validate_file` @ `ram:80033a3a` - Top-level file validation entry point
- `ncs_buffer_validator` @ `ram:8000ff0d` - Buffer validation wrapper
- `print_validation_report` @ `ram:80034a1f` - Outputs validation results

### Core Validation Functions
- `validate_header_and_feature_flags` @ `ram:8002c5cd` - Validates NCS header and feature flags
- `validate_timing_data` @ `ram:8002af02` - Validates session timing (tempo, swing, etc.)
- `validate_scenes_table` @ `ram:80029a52` - Validates scene definitions
- `validate_scene_chain_bounds_and_padding` @ `ram:8002866b` - Validates scene chain structure
- `validate_pattern_chain_table` @ `ram:80026e24` - Validates pattern chain table

### Synth Track Validation Functions
- `validate_synth_step_data` @ `ram:80023f28` - Validates synth step data
- `validate_synth_pattern_metadata` @ `ram:80022b32` - Validates synth pattern metadata
- `validate_synth_sync_rate` @ `ram:80021de5` - Validates synth sync rate settings
- `validate_synth_playback_direction` @ `ram:80021648` - Validates synth playback direction
- `validate_synth_automation_data` @ `ram:80020d23` - Validates synth automation data (complex nested structure)
- `validate_synth_track_settings` @ `ram:8001fe3c` - Validates synth track settings

### Drum Track Validation Functions
- `validate_drum_step_data` @ `ram:8001ddbd` - Validates drum step data
- `validate_drum_patterns_chunkB` @ `ram:8001cd64` - Validates drum pattern chunk B
- `validate_drum_patterns_chunkC` @ `ram:8001bf24` - Validates drum pattern chunk C
- `validate_drum_patterns_chunkD` @ `ram:8001b30f` - Validates drum pattern chunk D
- `validate_drum_patterns_chunkE` @ `ram:8001ab6a` - Validates drum pattern chunk E
- `validate_drum_mute_state_table` @ `ram:8001a31d` - Validates drum mute states
- `validate_default_drum_choices` @ `ram:80019bc3` - Validates default drum choices

### MIDI Track Validation Functions
- `validate_midi_patterns_chunkA` @ `ram:800172dd` - Validates MIDI pattern chunk A
- `validate_midi_patterns_chunkB` @ `ram:80016785` - Validates MIDI pattern chunk B
- `validate_midi_patterns_chunkC` @ `ram:80015fdd` - Validates MIDI pattern chunk C
- `validate_midi_patterns_chunkD` @ `ram:800158eb` - Validates MIDI pattern chunk D
- `validate_midi_patterns_chunkE` @ `ram:800150b5` - Validates MIDI pattern chunk E
- `validate_midi_track_settings` @ `ram:8001407d` - Validates MIDI track settings
- `validate_midi_keyboard_octaves` @ `ram:800123a4` - Validates MIDI keyboard octave settings

### Global Settings Validation Functions
- `validate_scale_root_and_type` @ `ram:800135cf` - Validates scale root and type settings
- `validate_delay_and_reverb_presets` @ `ram:80012b7b` - Validates delay and reverb presets

