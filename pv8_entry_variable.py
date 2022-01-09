from tkinter import *
root = Tk()
root.title("entery concept  ")
root.geometry("660x330")

user_l1=Label(root,text="username ->> ")
user_l1.grid(row=1,column=1)
pass_l1=Label(root,text="password ->> ")
pass_l1.grid(row=2,column=1)

user_input=StringVar          #thats means input in srting format
pass_input=StringVar          #thats means input in string format

username_entry=Entry(root,textvariable=user_input)
password_entry=Entry(root,textvariable=pass_input)

username_entry.grid(row=1,column=2)
password_entry.grid(row=2,column=2)

b1=Button(root,text="submit")
b1.grid(row=3,column=1)



root.mainloop()
