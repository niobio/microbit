
# Controlar un led amb la microbit

Aprendrem aquí com connectar una microbit a un protoboard i com encendre i apagar un LED, controlar la seva brillantor i també construirem un semáfor.


<div align="middle">
<video width="60%">
      <source src="img/leds_traffic.mp4" type="video/mp4">
</video></div>

Primer començarem per encendre un LED i després afegirem dos LED més per fer el semàfor.

## Material necessari
* microbit
* Protoboard
* Cables
* 3 LED (verd, groc, vermell)
* Resistències de 220 ohm

## Controlant un LED

Connecteu el resistor i el LED com mostra l'esquema inferior. Assegureu-vos que la pota més llarga del LED (terminal positiu) és el de l'esquerra. El resistor no té polaritat, per tent, no importa com el connecteu.

<div align="middle">
<img src="img/leds_breadboard_blink.png" width="50%">
</div>

La raó per la que connectem el resistor en sèrie amb el LED és limitar la intensitat de corrent que hi circula pel circuit i, d'aquesta manera, protegit el LED de sobreintensitats i evitar que peti.

El codi per fer funcionar el LED és el que s'observa a continuació


```python
from microbit import *
     
while True: 
        pin0.write_digital(1)  # turn pin0 (and the LED) on
        sleep(500)             # delay for half a second (500 milliseconds)
        pin0.write_digital(0)  # turn pin0 (and the LED) off
        sleep(500)             # delay for half a second
```

## Exercici

Feu un muntatge semblant amb tres LED per a simular el funcionament d'un semàfor.
