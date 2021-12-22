from tkinter import *
def changecolor(e):
    root.config(bg="red")
root=Tk()
root.geometry("200x200")
b1=Button(root,text="click me")
b1.bind("<Button>",changecolor)
b1.pack()
root.mainloop()