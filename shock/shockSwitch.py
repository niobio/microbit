from microbit import *

while True:
    # connectem la sortida del sensor al pin 6 de la microbit
    shock = pin6.read_digital()
    if shock == True:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
    sleep(500)
