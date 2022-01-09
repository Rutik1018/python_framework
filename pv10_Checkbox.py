from tkinter import *
root = Tk()
root.geometry("666x333")
root.title("creating the cheackbox ")

#Creating the cheakbox and set it
check1 = IntVar()
check2 = IntVar()
check3 = IntVar()

check1 = Checkbutton(root,text="male",variable=check1)
check1.grid(row=1,column=0)

check2 = Checkbutton(root,text="Female",variable=check2)
check2.grid(row=2)

check3 = Checkbutton(root,text="Others",variable=check3)
check3.grid(row=3)


root.mainloop()