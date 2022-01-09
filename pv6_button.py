from tkinter import *

root =Tk()
root.title("okk")
root.geometry("444x233")

frame_1=Frame(root,borderwidth=6,bg="green",relief=SUNKEN)
frame_1.pack(side=LEFT,anchor="nw")
b1=Button(frame_1,fg="red",text="print now ")
b1.pack(side=LEFT)
b2=Button(frame_1,fg="red",text="cancle ")
b2.pack(side=LEFT)
b3=Button(frame_1,fg="red",text=" back")
b3.pack(side=LEFT)
b4=Button(frame_1,fg="red",text="next")
b4.pack(side=LEFT,padx=20)





root.mainloop()


