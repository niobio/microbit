from microbit import *

while True:
    flame = pin4.read_digital()
    if flame == True:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
    sleep(500)
