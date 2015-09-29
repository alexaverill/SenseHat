from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
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
				[       R,O,O,R,R,R,R,O,
                                        R,O,O,R,O,O,R,O,
                                        R,O,O,R,O,O,R,O,
                                        R,R,R,R,R,R,R,O],
	
				[       O,O,O,O,O,O,O,O,
                                        O,R,R,R,R,R,O,O,
                                        O,R,O,O,O,O,O,O,
                                        O,R,O,O,O,O,O,O],

				[       R,R,R,R,R,R,R,O,
                                        R,O,O,R,O,O,R,O,
                                        R,O,O,R,O,O,R,O,
                                        R,R,R,R,R,R,R,O],

				[       R,R,R,R,R,R,R,O,
                                        R,O,O,R,O,O,O,O,
                                        R,O,O,R,O,O,O,O,
                                        R,R,R,R,O,O,O,O]	
				]
while(1==1):
	temp=sense.get_temperature()
	tempInt=int(temp)
	tempTens=int(tempInt/10)
	tempOnes=tempInt-(10*tempTens)
	FinalArray=displayValue[tempOnes]+displayValue[tempTens]
	sense.set_pixels(FinalArray)
	sleep(1)
