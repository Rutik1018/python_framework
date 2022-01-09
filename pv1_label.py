from tkinter import *
rutvik_root = Tk()
rutvik_root.geometry("444x234")  #the wimndow shows in this size
rutvik_root.minsize(300,250)     #the windows minimun size
rutvik_root.maxsize(800,700)     #the wimdow maximum size

l1 = Label(text="my short term goal is cricket and long term goal is cricket ....!")   # text label
l1.pack()                        #for label showing

rutvik_root.mainloop()