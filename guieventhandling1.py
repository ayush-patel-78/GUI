from tkinter import *
def showmsg():
    print("Welcome to python")

root=Tk()
root.geometry("200x200")
b1=Button(root,text="click me ",command=showmsg)
b1.pack()
root.mainloop()

