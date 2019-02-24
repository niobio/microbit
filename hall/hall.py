from microbit import *

while True:
    magnet = pin5.read_digital()
    if magnet == True:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
    sleep(500)
