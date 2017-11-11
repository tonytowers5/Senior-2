from tkinter import *
from tkinter import ttk
import sys

top = Tk()


# full screen
# top.attributes('-fullscreen', True)
top.geometry("1000x300")
# background color for the whole window
top.configure(background='black')
# title for window
top.title("Scent Select")

#defining functions

def exit():
	top.destroy()
	sys.exit()

def scent(button_state):
	print(button_state)
	#reset all
	scentButton1["text"] = "Scent 1 ON"
	scentButton2["text"] = "Scent 2 ON"
	scentButton3["text"] = "Scent 3 ON"
	scentButton4["text"] = "Scent 4 ON"
	scentButton5["text"] = "Scent 5 ON"
	scentButton6["text"] = "Scent 6 ON"

	#check and flip:
	#button1
	if(button_state == "Scent 1 OFF"):
		scentButton1["text"] = "Scent 1 ON"
	elif(button_state == "Scent 1 ON"):
		scentButton1["text"] = "Scent 1 OFF"
	#button2
	if(button_state == "Scent 2 OFF"):
		scentButton2["text"] = "Scent 2 ON"
	elif(button_state == "Scent 2 ON"):
		scentButton2["text"] = "Scent 2 OFF"
	#button3
	if(button_state == "Scent 3 OFF"):
		scentButton3["text"] = "Scent 3 ON"
	elif(button_state == "Scent 3 ON"):
		scentButton3["text"] = "Scent 3 OFF"
	#button4
	if(button_state == "Scent 4 OFF"):
		scentButton4["text"] = "Scent 4 ON"
	elif(button_state == "Scent 4 ON"):
		scentButton4["text"] = "Scent 4 OFF"
	#button5
	if(button_state == "Scent 5 OFF"):
		scentButton5["text"] = "Scent 5 ON"
	elif(button_state == "Scent 5 ON"):
		scentButton5["text"] = "Scent 5 OFF"
	#button6
	if(button_state == "Scent 6 OFF"):
		scentButton6["text"] = "Scent 6 ON"
	elif(button_state == "Scent 6 ON"):
		scentButton6["text"] = "Scent 6 OFF"
	'''
	if(button_num == 1):
		# check GPIO low or high
		scentButton1["text"] = "Scent 1 OFF"
	elif(button_num == 2):
		print("Scent 2 is ON")
	elif(button_num == 3):
		print("Scent 3 is ON")
	elif(button_num == 4):
		print("Scent 4 is ON")
	elif(button_num == 5):
		print("Scent 5 is ON")
	else:
		print("Scent 6 is ON")
	''' 

def powerSelect(button_num):
	
	lowButton["text"]= "Low"
	medButton["text"]= "Med"
	highButton["text"]= "High"

	if(button_num == 1):
		print("Low Temp")
		lowButton["text"]= "Low Selected"
	elif(button_num==2):
		print("Med Temp")
		medButton["text"]= "Med Selected"
	else:
		print("Hight Temp")
		highButton["text"]= "High Selected"


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


# scentButtons = [] 
# scentButtons.append("NOTHING")
# for i in range(1, 7):
# 	scentButton = Button(top, text="Scent" + str(i) + " ON", command = lambda: scent(i), height=5, width=20)
# 	scentButton.grid(row=0, column=(i-1)*5, padx=50)
# 	scentButtons.insert(i, scentButton)


lowButton = Button(top, text="Low", command = lambda: powerSelect(1), height=5, width=20)
lowButton.grid(row=1, column=5, padx=50)

medButton = Button(top, text="Med", command = lambda: powerSelect(2), height=5, width =20)
medButton.grid(row=1, column=15, padx=50)

highButton = Button(top, text="High", command = lambda: powerSelect(3), height=5, width=20)
highButton.grid(row=1, column=25, padx=50)






# # scentButton.place(x=15, y=10)

# high1 = Button(top, text="High", command= sel, height=2, width=8)
# high1.pack(side=BOTTOM)
# high1.place(x=15, y=55)

exitButton = Button(top, text="Exit", command = exit, height=3, width=10, bd=8)
exitButton.grid(row=2, columnspan=10)
exitButton.configure(background='red')

top.mainloop()