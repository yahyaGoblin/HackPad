import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

# ── Keys (4 direct-wired switches) ───────────────────────────────────────────
keyboard.matrix = KeysScanner(
    pins=[
        board.D0,  # SW1
        board.D1,  # SW2
        board.D2,  # SW3
        board.D3,  # SW4
    ],
    value_when_pressed=False,  # keys pull to GND
    pull=True,
)

# ── Encoder (SW7 only — clicky) ───────────────────────────────────────────────
encoder_handler = EncoderHandler()

encoder_handler.pins = (
    # (CLK/A,   DT/B,     SW,       is_inverted)
    (board.D4, board.D5, board.D6, False),  # SW7 — clicky encoder
)

keyboard.modules.append(encoder_handler)

# ── Keymap ────────────────────────────────────────────────────────────────────
# Key order: SW1, SW2, SW3, SW4
keyboard.keymap = [
    [
        KC.MPLY,  # SW1 — Play/Pause
        KC.MPRV,  # SW2 — Previous track
        KC.MNXT,  # SW3 — Next track
        KC.MUTE,  # SW4 — Mute
    ]
]

# Encoder actions per layer: (CW, CCW, press)
# SW7: CW = Vol↑, CCW = Vol↓, press = Mute
encoder_handler.map = [
    (
        (KC.VOLU, KC.VOLD, KC.MUTE),  # SW7 layer 0
    ),
]

# ── Go! ───────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    keyboard.go()
