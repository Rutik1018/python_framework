from tkinter import *
import tkinter.messagebox as tmsg
def func_submit():
     print(f"your age is {my_sliders.get()} ...thanks for visiting  !!!!!")
     tmsg.showinfo("your age ", f"your age is {my_sliders.get()} ...thank you !!!!!")

root= Tk()
root.geometry("444x444")
root.title("creating th sliders ")

l1=Label(root,text="what is your age ? ")
l1.pack()
#creatinmg  vertical the sliders
# my_sliders=Scale(root, from_=0,to=100)
# my_sliders.pack()

#creating the horizoantal sliders
my_sliders=Scale(root, from_=0,to=100, orient=HORIZONTAL,tickinterval=50)
my_sliders.set(18)
my_sliders.pack()

Button(root,text="submit",command=func_submit).pack()


root.mainloop()