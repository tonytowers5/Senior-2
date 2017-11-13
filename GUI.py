from tkinter import *
from tkinter import ttk
import sys

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO,OUT)
GPIO.output(40,GPIO.LOW)

GPIO.setup(11, GPIO,OUT)
GPIO.output(11,GPIO.LOW)

GPIO.setup(12, GPIO,OUT)
GPIO.output(12,GPIO.LOW)

GPIO.setup(13, GPIO,OUT)
GPIO.output(13,GPIO.LOW)

GPIO.setup(38, GPIO.OUT)
p = GPIO.PWM(38,1200)
p.start(0)


top = Tk()
#for sending binary bits to ports:
#you'll need wiringpy library ????
#the function youll use is digitalWrite(portNumber,portValue)

# full screen
# top.attributes('-fullscreen', True)
top.geometry("1000x300")
# background color for the whole window
top.configure(background='black')
# title for window
top.title("Scent Select")

#defining functions

def exit():
	p.stop()
	top.destroy()
	sys.exit()

#receives the text associated with the button clicked
def scent(button_state):
	print(button_state)
	#reset all
	scentButton1["text"] = "Scent 1 ON"
	scentButton2["text"] = "Scent 2 ON"
	scentButton3["text"] = "Scent 3 ON"
	scentButton4["text"] = "Scent 4 ON"
	scentButton5["text"] = "Scent 5 ON"
	scentButton6["text"] = "Scent 6 ON"

	scentButton1["background"] ='SystemButtonFace'
	scentButton2["background"] ='SystemButtonFace'
	scentButton3["background"] ='SystemButtonFace'
	scentButton4["background"] ='SystemButtonFace'
	scentButton5["background"] ='SystemButtonFace'
	scentButton6["background"] ='SystemButtonFace'
	#check and flip:
	if(GPIO.input(40)):
		pass
	#button1
	if(button_state == "Scent 1 OFF"):
		scentButton1["text"] = "Scent 1 ON"
		scentButton1["background"] ='SystemButtonFace'
		GPIO.output(40,GPIO.Low)
	elif(button_state == "Scent 1 ON"):
		scentButton1["text"] = "Scent 1 OFF"
		scentButton1["background"]='green'
		GPIO.output(40,GPIO.HIGH)

	#button2
	if(button_state == "Scent 2 OFF"):
		scentButton2["text"] = "Scent 2 ON"
		scentButton2["background"] ='SystemButtonFace'
		GPIO.output(40,GPIO.Low)
	elif(button_state == "Scent 2 ON"):
		scentButton2["text"] = "Scent 2 OFF"
		scentButton2["background"]='green'
		GPIO.output(40,GPIO.HIGH)
		
	#button3
	if(button_state == "Scent 3 OFF"):
		scentButton3["text"] = "Scent 3 ON"
		scentButton3["background"] ='SystemButtonFace'
		GPIO.output(40,GPIO.Low)
	elif(button_state == "Scent 3 ON"):
		scentButton3["text"] = "Scent 3 OFF"
		scentButton3["background"]='green'
		GPIO.output(40,GPIO.HIGH)

	#button4
	if(button_state == "Scent 4 OFF"):
		scentButton4["text"] = "Scent 4 ON"
		scentButton4["background"] ='SystemButtonFace'
		GPIO.output(40,GPIO.Low)
	elif(button_state == "Scent 4 ON"):
		scentButton4["text"] = "Scent 4 OFF"
		scentButton4["background"]='green'
		GPIO.output(40,GPIO.HIGH)

	#button5
	if(button_state == "Scent 5 OFF"):
		scentButton5["text"] = "Scent 5 ON"
		scentButton5["background"] ='SystemButtonFace'
		GPIO.output(40,GPIO.Low)
	elif(button_state == "Scent 5 ON"):
		scentButton5["text"] = "Scent 5 OFF"
		scentButton5["background"]='green'
		GPIO.output(40,GPIO.HIGH)

	#button6
	if(button_state == "Scent 6 OFF"):
		scentButton6["text"] = "Scent 6 ON"
		scentButton6["background"] ='SystemButtonFace'
		GPIO.output(40,GPIO.Low)
	elif(button_state == "Scent 6 ON"):
		scentButton6["text"] = "Scent 6 OFF"
		scentButton6["background"]='green'
		GPIO.output(40,GPIO.HIGH)

#receives a number based on the button clicked
def powerSelect(button_num):
	
	lowButton["text"]= "Low"
	medButton["text"]= "Med"
	highButton["text"]= "High"

	if(button_num == 1):
		print("Low Temp")
		lowButton["text"]= "Low Selected"
		p.ChangeDutyCycle(30)
	elif(button_num==2):
		print("Med Temp")
		medButton["text"]= "Med Selected"
		p.ChangeDutyCycle(60)
	else:
		print("Hight Temp")
		highButton["text"]= "High Selected"
		p.ChangeDutyCycle(97)


def sel():
	pass


# button 
scentButton1 = Button(top, text="Scent 1 ON", command = lambda: scent(scentButton1["text"]), height=5, width=20)
scentButton1.grid(row=0, column=0, padx=50)

scentButton2 = Button(top, text="Scent 2 ON", command = lambda: scent(scentButton2["text"]), height=5, width=20)
scentButton2.grid(row=0, column=5, padx=50)

# # button 3   
scentButton3 = Button(top, text="Scent 3 ON", command = lambda: scent(scentButton3["text"]), height=5, width=20)
scentButton3.grid(row=0, column=10, padx=50)

# # button 4
scentButton4 = Button(top, text="Scent 4 ON", command = lambda: scent(scentButton4["text"]), height=5, width=20)
scentButton4.grid(row=0, column=15, padx=50)

# # button 5
scentButton5 = Button(top, text="Scent 5 ON", command = lambda: scent(scentButton5["text"]), height=5, width=20)
scentButton5.grid(row=0, column=20, padx=50)

# #button 6
scentButton6 = Button(top, text="Scent 6 ON", command = lambda: scent(scentButton6["text"]), height=5, width=20)
scentButton6.grid(row=0, column=25, padx=50)




lowButton = Button(top, text="Low", command = lambda: powerSelect(1), height=5, width=20)
lowButton.grid(row=1, column=5, padx=50)
lowButton.configure(background = "yellow")

medButton = Button(top, text="Med", command = lambda: powerSelect(2), height=5, width =20)
medButton.grid(row=1, column=15, padx=50)
medButton.configure(background = "DarkOrange1")

highButton = Button(top, text="High", command = lambda: powerSelect(3), height=5, width=20)
highButton.grid(row=1, column=25, padx=50)
highButton.configure(background='firebrick3')






# # scentButton.place(x=15, y=10)

# high1 = Button(top, text="High", command= sel, height=2, width=8)
# high1.pack(side=BOTTOM)
# high1.place(x=15, y=55)

exitButton = Button(top, text="Exit", command = exit, height=3, width=30, bd=8)
exitButton.grid(row=2, column=15)
exitButton.configure(background='red')

top.mainloop()