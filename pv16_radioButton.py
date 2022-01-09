#creating the radio Button
from tkinter import *
import tkinter.messagebox as tmsg
def func_order():
    tmsg.showinfo("your order recived ", f"we have reciverd your order for {var.get()}")
root=Tk()
root.geometry("444x444")
root.title("radio button tutorail ")

var=IntVar()
# var.set(1)
Label(root,text="what would you like to have sir ? ",font="licida 19 bold", justify=LEFT,padx=15).pack()
radio = Radiobutton(root,text="veg",padx=15,variable=var,value=1).pack(anchor="w")
radio = Radiobutton(root,text="non veg ",padx=15,variable=var,value=2).pack(anchor="w")
radio = Radiobutton(root,text="nasta",padx=15,variable=var,value=3).pack(anchor="w")
radio = Radiobutton(root,text="fast food",padx=15,variable=var,value=4).pack(anchor="w")

Button(root,text="order now",command=func_order).pack()


root.mainloop()