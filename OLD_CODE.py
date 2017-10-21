from tkinter import*
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)
GPIO.setup(38, GPIO.OUT)

GPIO.setwarnings(False)

p = GPIO.PWM(38,1200)
p.start(0)
def sel(x):
    p.ChangeDutyCycle(int(x))


root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

def close_window():
    print("Exit Pressed")
    root.quit()
    p.stop()

def scent():
    print("Scent 1 Selected")
    if GPIO.input(40):
        GPIO.output(40,GPIO.LOW)
        scentButton["text"] = "Scent 1 ON"
    else:
        GPIO.output(40,GPIO.HIGH)
        scentButton["text"] = "Scent 1 OFF"

exitButton = Button(bottomFrame, text = "Exit" , command = close_window , height = 2, width = 6)
exitButton.pack(side = BOTTOM)

scentButton = Button(topFrame, text = "Scent 1 ON" , command = scent, height = 2, width = 8)
scentButton.pack()

var = DoubleVar()
slider1 = Scale(root, from_=100, to=0, variable = var , command = sel).pack()

root.mainloop()
GPIO.cleanup()

