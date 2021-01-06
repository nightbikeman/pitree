#!/usr/bin/python
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
import sys
from time import time
from random import random

class sequence:
    i=0.0
    step=0.01
    n=0
    count=0
    phase=0
    phases=3
    start = time()
    duration=30
    def __init__(self,master,n):
        self.master=master
        sequence.n+=1
        self.n=n

    def __iter__(self):
        return self

    def next(self):
        now=time()
        rnow = now % (24*60*60)
        if self.master:
            sequence.count = 0
            sequence.i += sequence.step
            if sequence.i > 1:
                sequence.i=1.0
                sequence.step= -sequence.step

            if sequence.i < 0:
                sequence.step= -sequence.step
                sequence.i=sequence.step

            if (now - sequence.start) > sequence.duration:
                sequence.phase = (sequence.phase+1) % sequence.phases
                sequence.start = now
                print "phase {0}".format(sequence.phase)

        if sequence.phase < 2:
            if sequence.count%2 == 0:
                c=sequence.i
            else:
                if sequence.phase == 0:
                    c=1-sequence.i
                else:
                    c=0
        if sequence.phase ==  2:
            c=random()

        # before 6:00 and between 9:00 and 16:00 turn lights off 
        # if ((rnow < 21600 ) or (( rnow > 32400 ) and ( rnow < 57600))):
        #if ((rnow < 21600 ) or (( rnow > 32400 ) and ( rnow < 58860))):
        #    c=0

        sequence.count += 1
        if c > 1.0 : c=1.0
        if c < 0.0 : c=0.0
        return c
    
#tree = LEDBoard(*range(2,28),pwm=True)
tree = LEDBoard( 15,2,12,7,20,8,23,22,21,14,11,18,17,24,19,9,3,10,6,5,4,25,16,13,pwm=True)

all = [range(0,26)]
rfaces=[[15,2,12],[23,22,21],[17,24,19],[6,5,4]]
lfaces=[[14,11,18],[9,3,10],[25,16,13],[7,20,8]]
faces=[[15,2,12],[7,20,8],[23,22,21],[14,11,18],[17,24,19],[9,3,10],[6,5,4],[25,16,13]]


tree.off()

m=True
z=0
for led in tree:
    s=sequence(m,z)
    z+=1
    m=False
    led.source = s
    

pause()
tree.off()
tree.close()
