import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

from digitalio import DigitalInOut, Direction, Pull
import board

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = 1
time.sleep(1)

class Key:    
    def __init__(self, pin):
        self.btn = DigitalInOut(pin)
        self.btn.direction = Direction.INPUT
        self.btn.pull = Pull.DOWN
        self.state = False

keyboard=Keyboard(usb_hid.devices)

keystate_a = False
keystate_b = False

key_a = Key(board.GP0)
key_b = Key(board.GP1)

def update():
    if key_a.btn.value != key_a.state:
        if key_a.state:
            keyboard.release(Keycode.A)
        else:
            keyboard.press(Keycode.A)
        key_a.state = key_a.btn.value
    if key_b.btn.value != key_b.state:
        if key_b.state:
            keyboard.release(Keycode.B)
        else:
            keyboard.press(Keycode.B)
        key_b.state = key_b.btn.value

led.value = 0

while True:
    update()
    time.sleep(0.05)