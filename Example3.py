# Show Message Example 
#This program will let you display a scrolling message on the LED matrix of the SenseHat

#import senseHat library
from sense_hat import SenseHat
# a library is a set of code that can be referenced in a program. It has books (functions) that can be opened to help with tasks. 

#we have to declare how we want to call the libary we imported. This will allow the program to use the books (functions) that are in the library
sense = SenseHat()

#now use the sense libary to open one of the books (functions) that it lets you use. 
#we want to show a message on the LED matrix 
sense.show_message("Hello World",text_colour=(0,0,255),scroll_speed=.5)

# Challenges:
# Can you make the LED display show your name?
