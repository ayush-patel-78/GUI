from tkinter import *
def changecolor1(e):
    root.config(bg="red")
def changecolor2(e):
    root.config(bg="blue")
root=Tk()
root.geometry("200x200")
b1=Button(root,text="click me")
b1.pack()
b1.bind("<Button-1>",changecolor1)
b1.bind("<Button-3>",changecolor2)
root.mainloop()