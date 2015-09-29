from sense_hat import SenseHat
sense= SenseHat()
sense.clear()
#take in inputs number1 operation number2
print 'Welcome to MathFun!'
number1=raw_input("Enter a number: ")
operation=raw_input("Enter + or -: ")
number2=raw_input("Enter another number: ")
output=0
oper=0
if(str(operation) == str("+")):
	output=int(number1)+int(number2)
	oper=1
if(str(operation)==str("-")):
	output=int(number1)-int(number2)
	oper=2
Red=[255,0,0]
#set row 1
for i in range(0,int(number1)):
	sense.set_pixel(0,i,Red)
#set row 2
if(oper==1):
	sense.set_pixel(1,0,[23,235,87])
else:
	sense.set_pixel(1,0,[84,94,23])
for i in range(0,int(number2)):
	sense.set_pixel(2,i,Red)
#setOutput
sense.set_pixel(3,0,[23,23,235])
for i in range(0,int(output)):
	sense.set_pixel(4,i,Red)
