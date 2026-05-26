# HACKPAD

A compact 6-key macropad powered by the RP2040, with two rotary encoders for scroll, zoom, or whatever feels useful that week. Fully custom PCB, hand-routed, with MX-compatible switch footprints at 19.05mm spacing.
This was the project that started everything — a Hack Club Hackpad build that turned into a crash course in KiCad, footprint libraries, PCB layout, and knowing when to scale back (and when not to). It taught the fundamentals that every later project relied on.

### Schematic Preview
<img width="1167" height="808" alt="image" src="https://github.com/user-attachments/assets/9a45358f-c970-4eb1-bbe9-ad0814f4368f" />

### PCB Preview
<img width="1277" height="656" alt="image" src="https://github.com/user-attachments/assets/6a04a904-dea7-45f5-9aa2-10bd841a1d6c" />


### 3D Model


## Features

- 6 mechanical key switches
- 2 rotary encoders
- Seeed XIAO MCU (small footprint, USB-C)
- Compact single PCB design

### Bill of Materials
 
| Component | Part | Quantity | Notes |
|---|---|---|---|
| Microcontroller | Seeed XIAO RP2040 | 1 | |
| Switches | MX-compatible mechanical switches | 6 | 5-pin or 3-pin |
| Keycaps | MX keycaps | 6 | |
| Rotary Encoders | EC11 rotary encoder | 2 | With push switch |
| Encoder Knobs | Any EC11-compatible knob | 2 | |
| PCB | Custom (this repo) | 1 | |
| USB Cable | USB-C | 1 | |
 
---
<img width="451" height="630" alt="comp" src="https://github.com/user-attachments/assets/49dd860b-e474-460d-be61-1096756b9771" />

## Fabrication

Gerber files are in the `/gerbers` folder, ready to send to JLCPCB, PCBWay, or your preferred fab.

## Firmware

Designed for use with [KMK](https://github.com/KMKfw/kmk_firmware) or [QMK](https://qmk.fm/) depending on the XIAO variant used.

## License

Open source hardware — feel free to modify and build your own.
