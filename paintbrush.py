from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
x=0
y=0
while True:
	r = 0
	g = 0
	b = 255
	color = (r,g,b)
	sense.set_pixel(x,y,color)
	for event in sense.stick.get_events():
        #print("Joystic was {} {}".format(event.action,event.direction))
		if(event.action=="pressed" and event.direction =="down"):
			if(y<7):#check to make sure pixel is in range
				y+=1 
        if(event.action=="pressed" and event.direction == "right"):
            if(x<7):
                x+=1
        if(event.action =="pressed" and event.direction == "up"):
            if(y>0):
                y-=1
        if(event.action == "pressed" and event.direction == "left"):
            if(x>0):
                x-=1

        if(event.action =="pressed" and event.direction =="middle"):
            sense.clear()

       
