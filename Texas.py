# Show Message Example 
#This program will let you display a scrolling message on the LED matrix of the SenseHat

#import senseHat library
from sense_hat import SenseHat
# a library is a set of code that can be referenced in a program. It has books (functions) that can be opened to help with tasks. 

#we have to declare how we want to call the libary we imported. This will allow the program to use the books (functions) that are in the library
sense = SenseHat()
#createa  blue variable
b= (0,0,0) #hold the color black
w=(255,255,255)
l= (0,0,255) #holds the color blue
p = (255,128,128)
o = (255,165,0)
#now use the sense libary we will use the set_pixel to make two blue pixels
sense.clear()
texas = [
b,b,o,o,b,b,b,b,
b,b,o,o,b,b,b,b,
b,b,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
b,o,o,o,o,o,o,o,
b,b,b,o,o,o,o,b,
b,b,b,o,o,b,b,b,
b,b,b,b,o,b,b,b
	]
sense.set_pixels(texas)
