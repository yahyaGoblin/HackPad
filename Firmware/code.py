import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# ── Matrix (direct-wired, no diodes needed for 6 keys) ──────────────────────
keyboard.col_pins = ()   # no matrix columns
keyboard.row_pins = ()   # no matrix rows

# Direct pin scan via keymap-less scanner — use KeysScanner instead
from kmk.scanners.keypad import KeysScanner

keyboard.matrix = KeysScanner(
    pins=[
        board.D0,  # SW1
        board.D1,  # SW2
        board.D2,  # SW3
        board.D3,  # SW4
        board.D7,  # SW5
        board.D8,  # SW6
    ],
    value_when_pressed=False,   # keys pull to GND
    pull=True,
)

# ── Encoders ─────────────────────────────────────────────────────────────────
encoder_handler = EncoderHandler()

encoder_handler.pins = (
    # (CLK/A,    DT/B,     SW,       is_inverted)
    (board.D4,  board.D5,  board.D6, False),   # SW7 — clicky encoder
    (board.D9,  board.D10, None,     False),   # SW8 — no switch
)

keyboard.modules.append(encoder_handler)

# ── Keymap ───────────────────────────────────────────────────────────────────
# Layer 0: default
# Key order: SW1, SW2, SW3, SW4, SW5, SW6
keyboard.keymap = [
    [
        KC.MPLY,    # SW1 — Play/Pause
        KC.MPRV,    # SW2 — Previous track
        KC.MNXT,    # SW3 — Next track
        KC.MUTE,    # SW4 — Mute
        KC.VOLD,    # SW5 — Volume down
        KC.VOLU,    # SW6 — Volume up
    ]
]

# Encoder actions per layer: (CW, CCW, press)
# SW7 (clicky): scroll up/down, press = mute
# SW8 (no click): volume up/down, press = None (ignored)
encoder_handler.map = [
    (
        (KC.VOLU, KC.VOLD, KC.MUTE),   # SW7 layer 0
        (KC.PGUP, KC.PGDN, KC.NO),     # SW8 layer 0
    ),
]

# ── Go! ──────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    keyboard.go()
