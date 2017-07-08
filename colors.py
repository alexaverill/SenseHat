from sense_hat import SenseHat
from random import randint
sense= SenseHat()
sense.clear()
red=randint(0,255)
green=randint(0,255)
blue=randint(0,255)
startColor=(red,green,blue)
colorArray = []
def setup():
	for x in range(0,64):
		colorArray.append((0,0,0))
def spiralColor(width,height,startColor):
	x = width
	y = height
	pos = 36
	colorArray[pos]=startColor
	count = 63
	while True:
		count -=1
		if(colorArray[pos+1] == (0,0,0)):
			pos = pos+9
		if(count == 0):
			break
		


def coloring(color,position):
	global red,green,blue
	if(position>=0 and position<=63):
		if(colorArray[position]==(0,0,0)):
			colorArray[position]=color
		percentDiff=100
		while(percentDiff>90):
			r=randint(0,255)
			g=randint(0,255)
			b=randint(0,255)
			average = ((r+g+b)+(red+green+blue))/2
			diff = (r+g+b)-(red+green+blue)
			percentDiff = diff/average
		red=r
		green = g
		blue = b
		coloring((red,green,blue),position-1)
	else:
		return
setup()
coloring((red,green,blue),63)
sense.set_pixels(colorArray)
#while True:
#	sense.set_pixels(colorArray)
	#for event in sense.stick.get_events():
		#if(event.action=="pressed" and event.direction=="middle"):
		#	sense.clear()
		#	coloring((randint(0,255),randint(0,255),randint(0,255)),63)
