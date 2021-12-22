from tkinter import *

def showname():
    fname=s1.get()
    lname=s2.get()
    l3.config(text=fname+" "+lname)
    
def fnquit():
    root.destroy() # this will only destroy root window if there is another window then that will not be destroyed 
root=Tk()
root.geometry("250x200")
l1=Label(root,text="First Name:")
l2=Label(root,text="Last Name:")
s1=StringVar()
s2=StringVar()
e1=Entry(root,textvariable=s1)
e2=Entry(root,textvariable=s2)
b1=Button(root,text="Show",command=showname)
b2=Button(root,text="Quit",command=fnquit)
l3=Label(root,textvariable="",font="Arial 14 bold")

l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
l3.grid(row=2,column=0,columnspan=2,sticky=W)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1,sticky=E)

root.mainloop()