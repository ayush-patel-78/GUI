from tkinter import *
def set_red_color(val):

    red=hex(int(sc1.get()))
    green=hex(int(sc2.get()))
    blue=hex(int(sc3.get()))
    
    red=red[2:]
    green=green[2:]
    blue=blue[2:]
    if len(red)==1:
        red="0"+red
    if len(green)==1:
        green="0"+green
    if len(blue)==1:
        blue="0"+blue
    
    color="#"+red+green+blue
    root.config(bg=color)
root=Tk()
root.geometry("200x200")
sc1=Scale(root,from_=0,to=255,orient=HORIZONTAL,command=set_red_color)
sc2=Scale(root,from_=0,to=255,orient=HORIZONTAL,command=set_red_color)
sc3=Scale(root,from_=0,to=255,orient=HORIZONTAL,command=set_red_color)

root.config(bg="#000000")
sc1.pack()
sc2.pack()
sc3.pack()
root.mainloop()