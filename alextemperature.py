from sense_hat import SenseHat
import math
sense = SenseHat()
sense.clear()
temperature = sense.get_temperature()
loop = math.floor(temperature)
print(loop)
x=0
while(x<=loop):
    sense.set_pixel(0,x,(0,255,0))
    x+=1

