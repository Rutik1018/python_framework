from tkinter import *
rutvik_root=Tk()
rutvik_root.title(" atributes  ...!")

rutvik_root.geometry("444x233")
#important label options
# text -add the text
# bg -background
# fg -foreground -mens text color
# font- sets and the font
# padx - x padding
# pady - y padding
# relif - boder style -SUNKEN,RAISED,GROOVE,RIDGE

l1=Label(text ='''tejas adhalrao tejas adhalrao\n tejas adhalraotejas \nadhalraotejas 
               adhalraotejas\n adhalraotejas adhal\nraotejas adhalrao''',bg="red",fg="white",padx=15,pady=30,font =("comicsansms",19,"bold"),
               borderwidth=5,relief=SUNKEN
        )

l1.pack()

rutvik_root.mainloop()