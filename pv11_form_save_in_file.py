from tkinter import *
def save_file():
    print(entry_game.get())
    with open("zmyfile.txt","a") as f:
        f.write(f"\nname of student >>> {entry_name.get()} \t game name of student >>> {entry_game.get()}\t age of students >>>{entry_age.get()}")

root = Tk()
root.geometry("666x333")
root.title("form save in file ....! ")

l_name=Label(text=" 1) what is your name ? ")
l_name.grid(row=1,column=1)
l_game=Label(text=" 2) which game  ?")
l_game.grid(row=2,column=1)
l_age=Label(text=" 3) what is your age ? ")
l_age.grid(row=3,column=1)

# var_name=StringVar
# var_game=StringVar
# var_age=StringVar

entry_name=Entry(root)
entry_name.grid(row=1,column=2)
entry_game=Entry(root)
entry_game.grid(row=2,column=2)
entry_age=Entry(root)
entry_age.grid(row=3,column=2)

Button(root,text="sumbit",bg="red",command=save_file).grid(row=4,column=1)

entry_name=Entry()



root.mainloop()
