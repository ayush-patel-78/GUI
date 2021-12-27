from tkinter import *

def changecolor():
    root.config(bg=strobj.get())

root=Tk()
old_color=root["bg"]
root.geometry("200x200")
strobj=StringVar()
cb=Checkbutton(root,text="Red",command=changecolor,variable=strobj,onvalue="red",offvalue=old_color)
cb.deselect()
cb.pack()
root.mainloop()