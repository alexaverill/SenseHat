from sense_hat import SenseHat
from time import sleep
import curses
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(1)
sense = SenseHat()
currentOption=0
R=[255,0,0]
O=[0,0,0]
displayValue=[                       [  O,O,R,R,R,R,O,O,
					O,R,O,O,O,O,R,O,
					O,R,O,O,O,O,R,O,
					O,O,R,R,R,R,O,O],

					[ O,O,O,O,O,O,O,O,
                                        O,O,O,O,O,O,O,O,
                                        O,R,R,R,R,R,R,O,
                                        O,O,O,O,O,O,O,O],	
				
				[       O,O,O,O,O,O,O,O,
                                        O,R,R,R,O,R,O,O,
                                        O,R,O,R,O,R,O,O,
                                        O,R,O,R,R,R,O,O],
			
				[       O,O,O,O,O,O,O,O,
                                        O,R,R,R,R,R,O,O,
                                        O,R,O,R,O,R,O,O,
                                        O,R,O,R,O,R,O,O],
		
				[       O,O,O,O,O,O,O,O,
                                        O,R,R,R,R,R,O,O,
                                        O,O,O,R,O,O,O,O,
                                        O,R,R,R,O,O,O,O],

			 	[       O,R,O,R,R,R,O,O,
                                        O,R,O,R,O,R,O,O,
                                        O,R,R,R,O,R,O,O,
                                        O,O,O,O,O,O,O,O],
				[       O,O,O,O,O,O,O,O,
                                        O,R,O,R,R,R,O,O,
                                        O,R,O,R,O,R,O,O,
                                        O,R,R,R,R,R,O,O],
	
				[       O,O,O,O,O,O,O,O,
                                        O,R,R,R,R,R,O,O,
                                        O,R,O,O,O,O,O,O,
                                        O,R,O,O,O,O,O,O],

				[       O,O,O,O,O,O,O,O,
                                        O,R,R,R,R,R,O,O,
                                        O,R,O,R,O,R,O,O,
                                        O,R,R,R,R,R,O,O],

				[       O,O,O,O,O,O,O,O,
                                        O,R,R,R,R,R,O,O,
                                        O,R,O,R,O,O,O,O,
                                        O,R,R,R,O,O,O,O]	
				]
while(1==1):
	c=screen.getch()
	if c == curses.KEY_UP:
		if currentOption==0:
			currentOption+=1
	if c == curses.KEY_DOWN:
		if currentOption==1:
			currentOption -=1
	temp=sense.get_temperature()
	if(currentOption==1):
		#convert from C to F
		temp=((temp*9)/5)+32
	tempInt=int(temp)
	tempTens=int(tempInt/10)
	tempOnes=tempInt-(10*tempTens)
	FinalArray=displayValue[tempOnes]+displayValue[tempTens]
	sense.set_pixels(FinalArray)
	sleep(1)
