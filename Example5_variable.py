# Show Message Example 
#This program will let you display a scrolling message on the LED matrix of the SenseHat

#import senseHat library
from sense_hat import SenseHat
# a library is a set of code that can be referenced in a program. It has books (functions) that can be opened to help with tasks. 

#we have to declare how we want to call the libary we imported. This will allow the program to use the books (functions) that are in the library
sense = SenseHat()
#createa  blue variable
blue = (0,0,255)
#now use the sense libary we will use the set_pixel to make two blue pixels
#sense.clear()
sense.set_pixel(3,0, blue)
sense.set_pixel(2,7,blue)

