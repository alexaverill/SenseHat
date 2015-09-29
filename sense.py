from sense_hat import SenseHat

sense = SenseHat()

#"Ball" will start centered 
ball_x=3
ball_y=4
X = [255,100, 0]  # Red
O = [255, 0, 100]  # White
field=[O]*64
for i in range(0,63):
	field[i]=O

sense.set_pixels(field)	
sense.set_pixel(ball_x,ball_y,X)
