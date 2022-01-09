from tkinter import *
def func1():
    print("its works buddy")
root = Tk()
root.geometry("444x444")
root.title("creating the help menu")

my_menu=Menu(root)      #Menu add into the root
m1=Menu(my_menu)
m1.add_command(label="help",command=func1)
m1.add_command(label="exit",command=func1)
m1.add_command(label="google",command=func1)


root.config(menu=my_menu)
my_menu.add_cascade(label="HELP",menu=m1) #main maenu heading  and add submenu

root.mainloop()