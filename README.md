# HACKPAD

A compact 6-key macropad with two potentiometers, built around the Seeed XIAO microcontroller. Great for shortcuts, media control, or custom workflows.

![PCB Preview](./images/preview.jpg)

## Features

- 6 mechanical key switches
- 2 potentiometers (volume, scroll, or any analog control)
- Seeed XIAO MCU (small footprint, USB-C)
- Compact single PCB design

## Bill of Materials

| Ref | Component | Value / Model | Qty |
|-----|-----------|---------------|-----|
| U1 | Microcontroller | Seeed XIAO (SAMD21 or RP2040) | 1 |
| SW1–SW6 | Mechanical Key Switch | Cherry MX compatible | 6 |
| RV1–RV2 | Potentiometer | 10kΩ linear | 2 |
| C1 | Decoupling Capacitor | 100nF 0402 | 1 |
| J1 | USB-C Connector | Built into XIAO | — |

> Part numbers are suggestions — swap for equivalents as needed.

## Fabrication

Gerber files are in the `/gerbers` folder, ready to send to JLCPCB, PCBWay, or your preferred fab.

Recommended specs:
- Layers: 2
- Thickness: 1.6mm
- Surface finish: HASL or ENIG

## Firmware

Designed for use with [KMK](https://github.com/KMKfw/kmk_firmware) or [QMK](https://qmk.fm/) depending on the XIAO variant used.

## Project Files

| File | Description |
|------|-------------|
| `macropad.kicad_sch` | Schematic |
| `macropad.kicad_pcb` | PCB layout |
| `/gerbers` | Fabrication files |

## License

Open source hardware — feel free to modify and build your own.