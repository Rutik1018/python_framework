from tkinter import *
from PIL import Image,ImageTk                      # for or showing the jpg images
rroot = Tk()

rroot.geometry("444x234")                          # window shows in this size

image = Image.open("Screenshots/1.jpg")            # by the image variable we can open the image
photo = ImageTk.PhotoImage(image)                  # in photo variable we stored the photo
l1 = Label(image=photo)                            # with the help of the lable we add the image
l1.pack()                                          # showing the label


rroot.mainloop()
