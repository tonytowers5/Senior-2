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
def scent(button_num):
	if(button_num == 1):
		print("Scent 1 is ON")
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

def sel():
	pass


# button 1
scentButton1 = Button(top, text="Scent 1 ON", command = lambda: scent(1), height=5, width=20).grid(row=0, column=0, padx=50)

# # button 2
scentButton2 = Button(top, text="Scent 2 ON", command = lambda: scent(2), height=5, width=20).grid(row=0, column=5, padx=50)

# # button 3   
scentButton3 = Button(top, text="Scent 3 ON", command = lambda: scent(3), height=5, width=20).grid(row=0, column=10, padx=50)

# # button 4
scentButton4 = Button(top, text="Scent 4 ON", command = lambda: scent(4), height=5, width=20).grid(row=0, column=15, padx=50)

# # button 5
scentButton5 = Button(top, text="Scent 5 ON", command = lambda: scent(5), height=5, width=20).grid(row=0, column=20, padx=50)

# #button 6
scentButton6 = Button(top, text="Scent 6 ON", command = lambda: scent(6), height=5, width=20).grid(row=0, column=25, padx=50)




#  # scentButton.place(x=15, y=10)

# high1 = Button(top, text="High", command= sel, height=2, width=8)
# high1.pack(side=BOTTOM)
# high1.place(x=15, y=55)

exitButton = Button(top, text="Exit", command = exit, height=3, width=10).grid(row=1, columnspan=10)

top.mainloop()