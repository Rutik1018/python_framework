from tkinter import *

rroot = Tk()

rroot.geometry("444x234")                                  #actual size of the frame
photo = PhotoImage(file="Screenshots/god.png")             #in photo vasriable images stored
l1 = Label(image=photo)                                    #help of label we can show the images
l1.pack()                                                  #for showing the images in frame


rroot.mainloop()
