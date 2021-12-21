from tkinter import *
import datetime
def showdate():    
    obj=datetime.datetime.now()
    str=obj.strftime("%d-%b-%Y, %H:%M:%S")
    l1.config(text=str)
    l1.pack()
root=Tk()
root.geometry("200x200")
b1=Button(root,text="Show date",command=showdate)
b1.pack()
l1=Label(root)
l1.pack()
root.mainloop()