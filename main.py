#event handling in the python
from tkinter import *

def myfunction(event):
    print("its work ")
    print(f" you clicked on the button at {event.x} and {event.y}")  #if click on the Button  its retun x and y event


root = Tk()
root.geometry("500x500")
root.title("evnets of Rutvik Adhalrao patil ")

b1=Button(root,text="please click me ")
b1.pack()

b1.bind('<Button-1>',myfunction)
b1.bind('<Button>',quit)   #right click to quite




root.mainloop()
