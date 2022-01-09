from tkinter import *
root = Tk()
root.title("this is about frame study......!!!")
root.geometry("665x633")

#creating the first fraame and ad  into the root
f1 = Frame(root, bg="yellow" , borderwidth=6 ,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y,pady=90)

#creating thhe second frame and add it into the rot
f2=Frame(root,borderwidth=9,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill=X)

#creating the labe 1 and add itto the frame one
l1=Label(f1,text="project tkinter - pycharm ")
l1.pack(pady=143)

#creating the second label and add it into the second frame
l2=Label(f2,text="welcome..............! ",font="Helvetica 22 bold " ,fg="red")
l2.pack()



root.mainloop()