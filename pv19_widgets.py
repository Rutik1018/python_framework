from tkinter import *
root=Tk()
height1=500
width1=850
root.geometry(f"{width1}x{height1}")
root.title("lets draw something new ")
#lets create the canvas
#this for drawing line , rectangle and  circle
can_widget=Canvas(root,width=width1,height=height1)
can_widget.pack()

#create the line
can_widget.create_line(0,0,850,500)     # x1 y1 and x2 y2

#creating the rectangle x1 y2 and x2 y2
can_widget.create_rectangle(10,250,300,400,fill="yellow")

#creating text and place it
can_widget.create_text(200,200,text="Rutvik adhalrao")


root.mainloop()