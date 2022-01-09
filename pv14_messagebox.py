from tkinter import *
import tkinter.messagebox as tmsg
def func_rate():
    print("rate us  ")
    value= tmsg.askquestion("How was your experiance ? "," c your experiance is god ?")
    print(value)
    if value=="yes":
        msg="Greate ...1 Thank you for rating us "
    else:
        msg="we will ask you after some time "
    tmsg.showinfo("feedback ",msg)

def func_help():
    print("i will help you ")
    tmsg.showinfo("help","i will help you broo ")
def func_google():
    print("google  ")


root = Tk()
root.geometry("444x444")
root.title("creating the help BOX ")

my_menu=Menu(root)      #Menu add into the root
m1=Menu(my_menu)
m1.add_command(label="help",command=func_help)
m1.add_command(label="rate us",command=func_rate)
m1.add_command(label="google",command=func_google)


root.config(menu=my_menu)
my_menu.add_cascade(label="HELP",menu=m1) #main maenu heading  and add submenu

root.mainloop()