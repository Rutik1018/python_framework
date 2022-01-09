from tkinter import *
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1

i=0
root=Tk()
root.geometry("444x444")
root.title("list box ...!!!!!!!!!!")

lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"first item of a list box")
Button(root,text="ADD ITEM ",command=add).pack()

root.mainloop()
