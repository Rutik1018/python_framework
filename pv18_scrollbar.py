#creating the scrollbar
from tkinter import *
root=Tk()
root.title("scroll bar tutorial ")
root.geometry("444x444")
#object of scrollbar
scrollbar_1=Scrollbar()
scrollbar_1.pack(side=RIGHT,fill=Y)
#text object
text=Text(root,yscrollcommand=scrollbar_1.set)
text.pack(fill=BOTH)

scrollbar_1.config(command=text.yview())



root.mainloop()