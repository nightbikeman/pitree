#!/usr/bin/python
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
import sys
import time

def face_on(f):
	for i in f:
	    tree[i].on()

def face_off(f):
	for i in f:
	    tree[i].off()

def face_value(f,v):
	for i in f:
	    tree[i].value=v

def face_rand(f,v):
	for i in f:
		tree[i].source_delay = v
		tree[i].source = random_values()

def drange(start, stop, step):
	r = start
	while r < (stop+step):
		yield r
		r += step

tree = LEDBoard(*range(2,28),pwm=True)
all = [range(0,26)]

rfaces=[[15,2,12],[23,22,21],[17,24,19],[6,5,4]]
lfaces=[[14,11,18],[9,3,10],[25,16,13],[7,20,8]]

faces=[[15,2,12],[7,20,8],[23,22,21],[14,11,18],[17,24,19],[9,3,10],[6,5,4],[25,16,13]]

for led in tree:
    led.off()

def rotate(count,d,faces):
	no_faces=len(faces)
	for c in range(0,count):
		tree[0].toggle()

		face_on(faces[c%no_faces])
		face_on(faces[(c+4)%no_faces])
		time.sleep(d)

		face_off(faces[c%no_faces])
		face_off(faces[(c+4)%no_faces])
		time.sleep(d)
		c=c+1

def fade_up_down(count,d,faces):
	no_faces=len(faces)
	for c in range(0,count):
		for i in drange(0.0,1.0,0.01):
			face_value(faces[c%no_faces],round(0.0+i,2))	
		time.sleep(d)
		for i in drange(0.0,1.0,0.01):
			face_value(faces[c%no_faces],round(1.0-i,2))	
		time.sleep(d)

def random(count,d,faces):
	no_faces=len(faces)
	for c in range(0,count):
		face_rand(faces[c%no_faces],0.1)	
		face_off(faces[(c+4)%no_faces])	
	time.sleep(c)

d=0.05
no_faces=len(faces)

d=[random,fade_up_down,rotate]
e=[faces,lfaces,rfaces,all]
while True:
	for t in e:
		for r in d:
			r(5,0.1,t)
	
pause()
