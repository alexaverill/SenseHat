import RPi.GPIO as GPIO
from array import *
import time
pinArray = array('i',[11,13,15,16,29,31,33,35])
restTime=.15
reps=3
def basicBlink(pins):
	for i in pins:
		GPIO.output(i,GPIO.LOW)
	time.sleep(restTime)
	for i in pins:
		GPIO.output(i,GPIO.HIGH)
	time.sleep(restTime)
	return
def rotateBlink(pins):
	totalPins=len(pins)
	startPoint=0
	endPoint=totalPins-1
	while(startPoint<=endPoint):
		GPIO.output(pins[startPoint],GPIO.LOW)
		time.sleep(restTime)
		GPIO.output(pins[startPoint],GPIO.HIGH)
		startPoint+=1

	return
def rotateAndBack(pins):
	totalPins=len(pins)
	startPoint=0
	endPoint=totalPins-1
	while(startPoint<=endPoint):
		GPIO.output(pins[startPoint],GPIO.LOW)
		time.sleep(restTime)
		GPIO.output(pins[startPoint],GPIO.HIGH)
		startPoint+=1
	while(endPoint>=0):
		GPIO.output(pins[endPoint],GPIO.LOW)
		time.sleep(restTime)
		GPIO.output(pins[endPoint],GPIO.HIGH)
		endPoint-=1
	return
def fillBar(pins):
	totalPins=len(pins)
	startPoint=0
	endPoint=totalPins-1
	while(startPoint<=endPoint):
		GPIO.output(pins[startPoint],GPIO.LOW)
		time.sleep(restTime)
		startPoint+=1
	return
def everyOther(pins):
	totalPins=len(pins)
	for i in range(0,totalPins):
		if(i%2==0):
			GPIO.output(pins[i],GPIO.LOW)
		else:
			GPIO.output(pins[i],GPIO.HIGH)
	time.sleep(restTime)
	return
def allLEDoff(pins):
	for i in pins:
		GPIO.output(i,GPIO.HIGH)
	return
def setup(pins):
	GPIO.setmode(GPIO.BOARD)
	for p in pins:
		GPIO.setup(p,GPIO.OUT)
	return	
setup(pinArray)
while(1==1):
	for i in range(0,reps):
		basicBlink(pinArray)
	for i in range(0,reps):
		rotateBlink(pinArray)
	for i in range(0,reps):
		rotateAndBack(pinArray)
	for i in range(0,reps):
		fillBar(pinArray)
		allLEDoff(pinArray)
	for i in range(0,reps*2):	
		everyOther(pinArray)
		allLEDoff(pinArray)
GPIO.cleanup()
