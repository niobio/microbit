from microbit import *

while True:
    flame = pin4.read_analog()
    display.scroll(flame)
    sleep(500))
