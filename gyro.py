from sense_hat import SenseHat

sense = SenseHat()
gyro_only = sense.get_gyroscope()
while(True):
	print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))

# alternatives
#print(sense.gyro)
#print(sense.gyroscope)
