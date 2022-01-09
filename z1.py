from tkinter import *
root= Tk()
root.title("my form ")
root.geometry("688x688")

lab_question = Label(root,text="question -->>> create a form to take a admission in dance class  using only button ,label & entry function ")
lab_title = Label(root,text="welcome to the dace class",fg="green",borderwidth=5,relief=SUNKEN,padx=20,pady=10)
lab_question.pack(anchor="nw")
lab_title.pack(side=TOP)


#form started
f2=Frame(root ,relief=GROOVE)
f2.pack(side=LEFT,fill=Y,pady=60)
lab_name=Label(f2,text="Enter your name : ")
lab_name.grid(row=3,column=2,pady=20)
lab_bdy=Label(f2,text="Enter your DOB : ")
lab_bdy.grid(row=4,column=2,pady=20)
lab_age=Label(f2,text="Enter your age : ")
lab_age.grid(row=5,column=2,pady=20)
lab_cantact=Label(f2,text="Enter your Contact number : ")
lab_cantact.grid(row=6,column=2,pady=20)
lab_parent=Label(f2,text="Enter your parent's name :")
lab_parent.grid(row=7,column=2,pady=20)
lab_par_contact=Label(f2,text="Enter parent's Contact : ")
lab_par_contact.grid(row=8,column=2,pady=20)
lab_fees=Label(f2,text="Enter fees you paid : ")
lab_fees.grid(row=9,column=2,pady=20)

#entry frame

f3=Frame(root,relief=GROOVE)
f3.pack(side=LEFT,fill=Y,pady=60)
entry_name=Entry(f3)
entry_name.grid(row=1,column=3,pady=20)
entry_bdy=Entry(f3)
entry_bdy.grid(row=2,column=3,pady=22)
entry_age=Entry(f3)
entry_age.grid(row=3,column=3,pady=20)
entry_contact=Entry(f3)
entry_contact.grid(row=4,column=3,pady=24)
entry_par_name=Entry(f3)
entry_par_name.grid(row=5,column=3,pady=22)
entry_par_con=Entry(f3)
entry_par_con.grid(row=6,column=3,pady=20)
entry_fees=Entry(f3)
entry_fees.grid(row=7,column=3,pady=20)

# butoon creating

b1=Button(f2,bg="yellow",text="  SUBMIT YOUR FORM  ")
b1.grid(row=10, column=1, pady=20)

b1=Button(f3,bg="red",text="  CLEAR FORM  ")
b1.grid(row=8, column=1, pady=20)

root.mainloop()
