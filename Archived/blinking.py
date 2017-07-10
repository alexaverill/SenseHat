import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)
gpio.output(7,True)
