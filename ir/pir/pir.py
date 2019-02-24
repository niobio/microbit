from microbit import *

while True:
    # Utilitzem em pin3 per llegir el sensor
    input_state = pin3.read_digital()  
    if input_state == True:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
    sleep(500)
