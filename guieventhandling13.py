from tkinter import *
def changecolor(e):
    ch=e.char
    if ch=="r":
        root.config(bg="red")
    elif ch=="g":
        root.config(bg="green")
    elif ch=="b":
        root.config(bg="blue")
root=Tk()
root.geometry("200x200+100+200")
root.bind("<Key>",changecolor)
root.mainloop()