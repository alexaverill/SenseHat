from sense_hat import SenseHat
from random import randint
sense = SenseHat()
sense.low_light = True
sense.clear()
x=0
y=0
r=0
g=0
b=255
while True:
	color=(r,g,b)
	sense.set_pixel(x,y,color)
	for event in sense.stick.get_events():
		if(event.action == "pressed" and event.direction == "left"):
			if(x>0):
				x-=1
		if( event.action == "pressed" and event.direction == "right"):
			if(x<7):
				x+=1
		if(event.action == "pressed" and event.direction =="down"):
			if(y<7):
				y+=1
		if(event.action == "pressed" and event.direction == "up"):
			if(y>0):
				y-=1
		if(event.action == "pressed" and event.direction =="middle"):
			r=randint(0,255)
			g=randint(0,255)
			b=randint(0,255)
