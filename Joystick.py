from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()
black=(0,0,0)
x=0
y=0
while True:
    sense.set_pixel(x,y,(0,0,255))
    for event in sense.stick.get_events():
        #print("Joystic was {} {}".format(event.action,event.direction))
        if(event.action=="pressed" and event.direction =="down"):
            if(y<7):#check to make sure pixel is in range
                sense.set_pixel(x,y,black)#clear previous pixel
		y+=1 
        if(event.action=="pressed" and event.direction == "right"):
            if(x<7):
		sense.set_pixel(x,y,black)
                x+=1
        if(event.action =="pressed" and event.direction == "up"):
            if(y>0):
		sense.set_pixel(x,y,black)
                y-=1
        if(event.action == "pressed" and event.direction == "left"):
            if(x>0):
		sense.set_pixel(x,y,black)
                x-=1

        if(event.action =="pressed" and event.direction =="middle"):
            sense.clear()
                
               
       
