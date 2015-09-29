from sense_hat import SenseHat
from time import sleep
import math
sense = SenseHat()
sense.set_imu_config(False, False, True)
#start by setting a "level" state
base_level=sense.get_orientation_degrees()
base_pitch=base_level['pitch']
base_roll=base_level['roll']
#base_yaw=base_level['yaw']
bx=3
by=4
diffV=1
X=[255,100,0]
S=[0,0,0]
field=[S]*64
while(True):
	orien = sense.get_orientation_degrees()
	pdiff=orien['pitch']-base_pitch
	rdiff=orien['roll']-base_roll
	print '{} {} {}'.format(orien['pitch'],base_pitch,pdiff)
	print '{} {} {}'.format(orien['roll'],base_roll,rdiff)
	#print '{} {}'.format(orien['yaw'],base_yaw)
	print'######################################'	
	if(pdiff> diffV):
		if(bx>0):
			bx-=1
	elif(pdiff < -diffV):
		if(bx<7):
			bx+=1
	if(rdiff >diffV):
		if(by<7):	
			by+=1
	elif(rdiff < -diffV):
		if(by >0):
			by-=1
	for i in range(0,63):
		field[i]=S
	sense.set_pixels(field)
	sense.set_pixel(bx,by,X)
	sleep(1)
