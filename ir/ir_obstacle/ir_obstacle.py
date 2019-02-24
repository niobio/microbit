from microbit import *

while True:
    detect = pin5.read_digital()
    if detect == True:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
    sleep(500)
