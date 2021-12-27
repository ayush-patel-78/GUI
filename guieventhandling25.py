from tkinter import *

def show():
    print(strobj.get())

root=Tk()
old_color=root["bg"]
root.geometry("200x200")
strobj=StringVar()
cb=Checkbutton(root,text="Red",command=show,variable=strobj,onvalue="hi",offvalue="bye")
cb.deselect()
cb.pack()
root.mainloop()