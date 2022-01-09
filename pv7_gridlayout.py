from tkinter import *
root = Tk()
root.title("grid layout...!")
root.geometry("660x333")

l1=Label(root,text="user name")
l2=Label(root,text="Password")
l1.grid(row=1,column=1)
l2.grid(row=2,column=1)

root.mainloop()