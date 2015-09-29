from sense_hat import SenseHat
sense = SenseHat()
temp = sense.get_temperature()
R=[255,0,0]
O=[94,28,28]
displayValue=[                       [  O,O,R,R,R,R,O,O,
					O,R,O,O,O,O,R,O,
					O,R,O,O,O,O,R,O,
					O,O,R,R,R,R,O,O],

					[ O,O,O,O,O,O,O,O,
                                        O,O,O,O,O,O,O,O,
                                        O,R,R,R,R,R,R,O,
                                        O,O,O,O,O,O,O,O],	
				
				[          R,R,R,R,O,O,R,O,
                                        R,O,O,R,O,O,R,O,
                                        R,O,O,R,O,O,R,O,
                                        R,O,O,R,R,R,R,O],
			
				[         R,R,R,R,R,R,R,O,
                                        R,O,O,R,O,O,R,O,
                                        R,O,O,R,O,O,R,O,
                                        R,O,O,R,O,O,R,O],
		
				[          R,R,R,R,R,R,R,0,
                                        O,O,O,R,O,O,O,O,
                                        O,O,O,R,O,O,O,O,
                                        R,R,R,R,O,O,O,O],
			 	[          R,O,O,R,R,R,R,O,
                                        R,O,O,R,O,O,R,O,
                                        R,O,O,R,O,O,R,O,
                                        R,R,R,R,O,O,R,O],
				[          R,O,O,R,R,R,R,O,
                                        R,O,O,R,O,O,R,O,
                                        R,O,O,R,O,O,R,O,
                                        R,R,R,R,R,R,R,O],
	
				[          R,R,R,R,R,R,R,0,
                                        R,O,O,O,O,O,O,O,
                                        R,O,O,O,O,O,O,O,
                                        R,O,O,O,O,O,O,O],

				[          R,R,R,R,R,R,R,0,
                                        R,O,O,R,O,O,R,O,
                                        R,O,O,R,O,O,R,O,
                                        R,R,R,R,R,R,R,O],

				[          R,R,R,R,R,R,R,0,
                                        R,O,O,R,O,O,O,O,
                                        R,O,O,R,O,O,O,O,
                                        R,R,R,R,O,O,O,O]	
				]
tempInt=int(temp)
tempTens=int(tempInt/10)
tempOnes=tempInt-(10*tempTens)
FinalArray=displayValue[tempOnes]+displayValue[tempTens]

print(FinalArray)
sense.set_pixels(FinalArray)
#sense.show_message(str(int(temp)))
