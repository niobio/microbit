
# Pins d'entrada/sortida

La placa micro:bit té una banda amb connectors que permeten comunicar-se amb dispositius connectats a la micro:bit. Alguns connectors són accessibles amb clips cocodril (P0, P1, P2, 3V i GND), però hi ha d'altres que són molt prims i que, per fer-los servir, necessitem afegir un accessori que els faci accessibles, nosaltres utilitzarem la placa motor:bit (veure [Controlant motors](https://niobio.github.io/microbit/motor/motors.html)) per a poder accedir a tots els pins.

La especificació de l'ús de cada pin es pot veure a la figura inferior.

<div align="middle">
<img src="img/pinout.png" width="80%">
</div>

## Entrades tàctils

Els pins 0, 1 i 2 poden detactar quan toquem els terminals, ja que tenen un sensor tàctil capacitiu incorporat. Per utilitzar aquests pins podem escriure el codi següent:

`is_touched()`

Aquesta funció retorna `True` si toquem el terminal i `False` si no el toquem.

## Entrades i sortides digitals

Tots els pins es poden fer servir com entrades i sortides digitals. Per exemple, per llegir l'entrada digital del pin 3 podem utilitzar l'ordre següent:

`pin3.read_digital()`

que entregarà el valor `1` si el valor de l'entrada correspon a un valor de voltatge alt i `0` per a un voltatge baix.

En el cas de les sortides digitals podem fer servir l'ordre:

`pin3.write_digital(x)`

que escriu el valor `x` en el pin 3, on `x` pot tenir el valor `0` o `1`.


## Entrades i sortides analògiques

Els pins 0, 1, 2, 3, 4 i 10 poden fer-se servir com entrades analògiques. Un exemple d'ús en el codi per llegir l'entrada del pin 0 podria ser:

`pin0.read_analog()`

Els pins de la placa microbit no pot donar voltatges de sortida analògics, es a dir, no pot entregar diferents voltatge, en canvi pot donar 0V o 3,3V. Per a canviar la velocitat d'un motor o el grau d'il·luminació d'un LED el que fa la placa és simular un voltatge variable a través d'un mètode que es diu Modulació d'Amplada de Pols, PWM en les seves segles en anglès (Pulse-Width Modulation), i que consisteix en injectar polses de diferent amplada com es veu a la figura inferior.

<div align="middle">
<img src="img/pwm.png" width="80%">
</div>

Tots els polses tenen el mateix període però es varia l'amplada del pols i això fa que la potència entregada a l'actuador sigui més alta quan el pols és més ample, com a conseqüència, el motor anirà més ràpid o el LED brillarà més quan el pols té una amplada més gran.

Per activar una sortida analògica en el pin 4, per exemple, fem servir l'ordre:

`pin4.write_analog(n)`

on `n` és un nombre enter que pot prendre 1024 valors possibles, començant per 0 (corresponent a 0V) fins al 1023 (corresponent a un voltatge de 3,3V).
