from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
def showopen():
    sel_color=colorchooser.askcolor(color="#00ffff",title="Select a color")
    if sel_color[0] is None:
            messagebox.showinfo("color","U did not select any color")
    else:
            lbl.config(text=sel_color)
            root.config(bg=sel_color[1])
root=Tk()
root.geometry("600x300")
btn=Button(root,text="Choose color",command=showopen)
lbl=Label(root,text="Selected color appear here ")
btn.pack()
lbl.pack()
root.mainloop()