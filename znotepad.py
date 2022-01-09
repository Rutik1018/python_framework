from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import  askopenfilename ,asksaveasfilename
import os

def newfile():
    global  file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0,END)     #1.0 fisrt line -to- 0th character  DELETE all
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents","*.*")])
                         #open any file in txt format
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file)+ " -  Notepad")  #from file path take file name only and add next - Notepad
        textarea.delete(1.0, END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents","*.*")])
        if file == "":      #if dont select the file
            file=None
        else:
           #if we select file save it
           f=open(file,"w")
           f.write(textarea.get(1.0,END))
           f.close()
           root.title(os.path.basename(file)+ " - Notepad ")   #take file name from file path and add next - NOtepad

    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def quitapp():
    root.destroy()

def cut():
    textarea.event_generate(("<<Cut>>"))     #tkinter handle itself copy cut and paste function
def copy():
    textarea.event_generate(("<<Copy>>"))     #tkinter handle itself copy cut and paste function
def paste():
    textarea.event_generate(("<<Paste>>"))       #tkinter handle itself copy cut and paste function
def about():
    showinfo("Notepad","notepad by - Rutvik Adhlarao \n python devloper \n cricketer")   #frame title and message

def darkmode():
    textarea.configure(background="grey")
def lightmode():
    textarea.configure(background="white")
def yellowmode():
    textarea.configure(background="yellow")
def redkmode():
    textarea.configure(background="red")

if __name__ == '__main__':
    root=Tk()
    root.title("my notepad")
    root.geometry("644x688")

#adding the text area
    textarea= Text(root,font="lucida 13 ")
    textarea.pack(expand=True,fill=BOTH)
    file=None
#creating the menubar   #file menu start
    menubar=Menu(root)
    filemenus = Menu(menubar,tearoff=0)
    #open the new file
    filemenus.add_command(label="NEW",command=newfile)
    #to open  already save file
    filemenus.add_command(label="Open",command=openfile)
    #to save the currenty file
    filemenus.add_command(label="Save",command=savefile)
    filemenus.add_separator()
    filemenus.add_command(label="Exit", command=quitapp)
    menubar.add_cascade(label="FILE",menu=filemenus)

    #file menu end

#edit menu start here
    editmenu=Menu(menubar,tearoff=0)
    #cut copy and paste
    editmenu.add_command(label ="Cut",command=cut)
    editmenu.add_command(label ="Copy",command=copy)
    editmenu.add_command(label ="Paste",command=paste)
    menubar.add_cascade(label="EDIT",menu=editmenu)
    #edit menu eds

#Help menu Starts
    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label="About Notepad",command=about)
    menubar.add_cascade(label="HELP",menu=helpmenu)
    root.config(menu=menubar)

#adding the scrollbar
    scrollbar_1=Scrollbar(textarea)
    scrollbar_1.pack(side=RIGHT,fill=Y)
    scrollbar_1.config(command=textarea.yview)   #equal to textarea y legth
    textarea.config(yscrollcommand=scrollbar_1.set)
#aaadiing dark mode
    darkmenu=Menu(menubar,tearoff=0)
    #cut copy and paste
    darkmenu.add_command(label ="DARK MODE",command=darkmode)
    darkmenu.add_command(label ="LIGHT MODE",command=lightmode)
    darkmenu.add_command(label ="RED MODE",command=redkmode)
    darkmenu.add_cascade(label="YELLOW MODE",menu=yellowmode)
    menubar.add_cascade(label="MODE",menu=darkmenu)


    root.mainloop()