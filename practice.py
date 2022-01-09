from tkinter import *
root =Tk()
h=400
w=500
root.geometry("444x444")
root.title("its label turorial")

l1=Label(root,text="my Newspaper is here ",font =("comisanss",22,"bold"),bg="yellow",fg="green",borderwidth=10,relief=SUNKEN,padx=100)
l1.pack()
l2=Label(root,text="whta is your name ",font=("timesinRoman",30,"bold"))
l2.grid(row=1,column=1)


root.mainloop()