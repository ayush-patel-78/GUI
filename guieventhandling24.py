from tkinter import *

def changecolor():
    if intobj.get()==1:
        root.config(bg="#ff0000")
    else:
        root.config(bg=old_color)

root=Tk()
old_color=root["bg"]
root.geometry("200x200")

intobj=IntVar()
cb=Checkbutton(root,text="Red",command=changecolor,variable=intobj)
cb.pack()
root.mainloop()