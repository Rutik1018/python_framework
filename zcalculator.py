from  tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())                  #convert into int
        else:
            try:
                value= eval(screen.get())
            except Exception as e:
                scvalue.set("Error..........!!!")
                screen.update()

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()
root.geometry("644x600")
root.title("my calulator")
#creating the status bar
Label(root,text="code by-->> Rutvik Adhalrao ",bg="gray").pack(side=BOTTOM,fill=X)

scvalue=StringVar()
scvalue.set("")
screen= Entry(root,textvar=scvalue,font="lucida 40 bold",borderwidth=6,relief=RIDGE)
screen.pack(fill=X,padx=20,pady=20)
frame_main=Frame(root, borderwidth=5,relief=RIDGE)
frame_main.pack()
#frame started  9 8 7 +
f1=Frame(frame_main, bg="yellow")    #frame started
b9=Button(f1,text="9",font="lucida 30 bold",padx=20,pady=10)
b9.pack(side=LEFT,padx=15,pady=5)
b9.bind("<Button-1>",click)

b8=Button(f1,text="8",font="lucida 30 bold",padx=20,pady=10)
b8.pack(side=LEFT,padx=15,pady=5)
b8.bind("<Button-1>",click)

b7=Button(f1,text="7",font="lucida 30 bold",padx=20,pady=10)
b7.pack(side=LEFT,padx=15,pady=5)
b7.bind("<Button-1>",click)

b=Button(f1,text="+",font="lucida 30 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
f1.pack()    #frame ended

#button 6,5,4 -
f1=Frame(frame_main, bg="yellow")    #frame started
b6=Button(f1,text="6",font="lucida 30 bold",padx=20,pady=10)
b6.pack(side=LEFT,padx=15,pady=5)
b6.bind("<Button-1>",click)

b5=Button(f1,text="5",font="lucida 30 bold",padx=20,pady=10)
b5.pack(side=LEFT,padx=15,pady=5)
b5.bind("<Button-1>",click)

b4=Button(f1,text="4",font="lucida 30 bold",padx=20,pady=10)
b4.pack(side=LEFT,padx=15,pady=5)
b4.bind("<Button-1>",click)

b=Button(f1,text="-",font="lucida 30 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f1.pack()    #frame ended

#button 3,2,1 *
f1=Frame(frame_main, bg="yellow")    #frame started
b3=Button(f1,text="3",font="lucida 30 bold",padx=20,pady=10)
b3.pack(side=LEFT,padx=15,pady=5)
b3.bind("<Button-1>",click)

b2=Button(f1,text="2",font="lucida 30 bold",padx=20,pady=10)
b2.pack(side=LEFT,padx=15,pady=5)
b2.bind("<Button-1>",click)

b1=Button(f1,text="1",font="lucida 30 bold",padx=20,pady=10)
b1.pack(side=LEFT,padx=15,pady=5)
b1.bind("<Button-1>",click)

b=Button(f1,text="*",font="lucida 30 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f1.pack()    #frame ended





#button 0 ,c, =,/
f1=Frame(frame_main, bg="yellow")    #frame started
b3=Button(f1,text="0",font="lucida 30 bold",padx=20,pady=10)
b3.pack(side=LEFT,padx=15,pady=5)
b3.bind("<Button-1>",click)

b2=Button(f1,text="C",font="lucida 30 bold",padx=20,pady=10)
b2.pack(side=LEFT,padx=15,pady=5)
b2.bind("<Button-1>",click)

b1=Button(f1,text="=",font="lucida 30 bold",padx=20,pady=10)
b1.pack(side=LEFT,padx=10,pady=5)
b1.bind("<Button-1>",click)

b=Button(f1,text="/",font="lucida 30 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f1.pack()    #frame ended

root.mainloop()
