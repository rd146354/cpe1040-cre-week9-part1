from microbit import *

while True:
    curtime = running_time()
    pressed_time = 0
    while button_a.is_pressed():
        pressed_time = running_time() - curtime
    if pressed_time > 500:
        display.scroll("Greater than 500")
    elif pressed_time > 0:
        display.scroll("Less than 500")

