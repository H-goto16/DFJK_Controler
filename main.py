import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

def keyInput(keycodeName):
    keyboard.send(keycodeName)

keyboard = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
fbutton = digitalio.DigitalInOut(board.GP13)
fbutton.switch_to_input(pull=digitalio.Pull.DOWN)
dbutton = digitalio.DigitalInOut(board.GP12)
dbutton.switch_to_input(pull=digitalio.Pull.DOWN)
jbutton = digitalio.DigitalInOut(board.GP11)
jbutton.switch_to_input(pull=digitalio.Pull.DOWN)
kbutton = digitalio.DigitalInOut(board.GP10)
kbutton.switch_to_input(pull=digitalio.Pull.DOWN)
led.value = False

while True:
    if fbutton.value:
        led.value = True
        keyInput(Keycode.F)
        led.value = False
    elif dbutton.value:
        led.value = True
        keyInput(Keycode.D)
        led.value = False
    elif jbutton.value:
        led.value = True
        keyInput(Keycode.J)
        led.value = False
    elif kbutton.value:
        led.value = True
        keyInput(Keycode.K)
        led.value = False
        
