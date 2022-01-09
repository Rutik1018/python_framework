#remove the line and seprated the menu
from tkinter import *

def myfunction():
    print("okkkkkkkkkkaaaaaaaaaaaaayyyyyyyyyyyy")


root=Tk()
root.title("creating the menu ")
root.geometry("666x333")
#new menu creating
yourmenu_bar=Menu(root)

m1=Menu(yourmenu_bar,tearoff=0)     # remov line using the tearoff
m1.add_command(label="save",command=myfunction)
m1.add_command(label="save as ",command=myfunction)
m1.add_command(label="print ",command=myfunction)
m1.add_separator()
m1.add_command(label="open ",command=myfunction)
root.config(menu=yourmenu_bar)

yourmenu_bar.add_cascade(label="FILE",menu=m1)


root.mainloop()