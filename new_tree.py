#!/usr/bin/python
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
import sys
import time

tree = LEDBoard(*range(2,28),pwm=True)

rfaces=[[15,2,12],[23,22,21],[17,24,19],[6,5,4]]
lfaces=[[14,11,18],[9,3,10],[26,16,13],[7,20,8]]

faces=[[15,2,12],[7,20,8],[23,22,21],[14,11,18],[25,16,13],[9,3,10],[6,5,4],[17,24,19]]

for led in tree:
    led.off()

while True:
    for f in faces:
        for i in f:
            tree[i].on()
        tree[0].toggle()
        time.sleep(0.1)
        for i in f:
            tree[i].off()
        time.sleep(0.1)
pause()
