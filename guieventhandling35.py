from tkinter import *
def set_red_color(val):
    red=hex(int(val))
    red=red[2:]
    if len(red)==1:
        red="0"+red
    color="#"+red+"0000"
    root.config(bg=color)
root=Tk()
root.geometry("200x200")
sc=Scale(root,from_=0,to=255,orient=HORIZONTAL,command=set_red_color)
root.config(bg="#000000")
sc.pack()
root.mainloop()