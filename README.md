# HACKPAD
A compact 4-key macropad powered by the Seeed XIAO, with a rotary encoder for volume, scroll, or whatever feels useful that week. Fully custom PCB, hand-routed, with MX-compatible switch footprints at 19.05mm spacing.
This was the project that started everything — a Hack Club Hackpad build that turned into a crash course in KiCad, footprint libraries, PCB layout, and knowing when to scale back (and when not to). It taught the fundamentals that every later project relied on.
### Schematic Preview
<img width="1127" height="740" alt="image" src="https://github.com/user-attachments/assets/819baba3-48df-408a-8e86-8d009179d163" />
### PCB Preview
<img width="1088" height="587" alt="image" src="https://github.com/user-attachments/assets/cd291c53-0ab9-41be-9bee-8df363ebcbc8" />
### 3D Model
<img width="1137" height="620" alt="image" src="https://github.com/user-attachments/assets/5696c03d-3a10-4487-9385-9a175eff86f6" />
## Features
- 4 mechanical key switches
- 1 rotary encoder (clicky, EC11)
- Seeed XIAO MCU (small footprint, USB-C)
- Compact single PCB design

### Bill of Materials
| Component | Part | Quantity | Notes | Link | Distributor |
|---|---|---|---|---|---|
| Microcontroller | Seeed XIAO RP2040 | 1 | | [Link](https://keebd.com/products/xiao-rp2040-controller?_pos=1&_psq=xiao&_ss=e&_v=1.0) | KEEBD |
| Switches | MX-compatible mechanical switches (Gateron Blue) | 4 | 5-pin or 3-pin | [Link](https://keebd.com/products/gateron-blue) | KEEBD |
| Keycaps | MX keycaps | 4 | | — | local |
| Rotary Encoder | EC11 rotary encoder | 1 | With push switch | [Link](https://keebd.com/products/ec11-encoder-with-switch?_pos=1&_psq=enco&_ss=e&_v=1.0) | KEEBD |
| Encoder Knob | 3D Printed EC11-compatible knob | 1 | | [Link](https://keebd.com/products/3d-printed-encoder-knob?variant=40383061917848) | KEEBD |
| PCB | Custom (this repo) | 1 | Gerbers in `/gerbers` | — | PCBWay |
| Baseplate | Laser cut / 3D printed | 1 | Holds the PCB | — | local |
| USB Cable | USB-C | 1 | | — | local |

---
<img width="609" height="735" alt="image" src="https://github.com/user-attachments/assets/103a84cd-9188-44d5-8f01-c776632f08d6" />
## Fabrication
Gerber files are in the `/gerbers` folder, ready to send to JLCPCB, PCBWay, or your preferred fab.
## Firmware
Designed for use with [KMK](https://github.com/KMKfw/kmk_firmware). See `code.py` for the full config — 4 keys mapped to media controls, encoder for volume with mute on press.
## License
Open source hardware — feel free to modify and build your own.
