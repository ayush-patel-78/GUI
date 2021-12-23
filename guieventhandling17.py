from tkinter import *

def showname():
    fname=e1.get()
    lname=e2.get()
    e3.delete(0,END)
    e3.insert(0,fname+" "+lname)
    
def fnquit():
    root.destroy() # this will only destroy root window if there is another window then that will not be destroyed 
root=Tk()
root.geometry("250x200")
l1=Label(root,text="First Name:")
l2=Label(root,text="Last Name:")

e1=Entry(root)
e2=Entry(root)
b1=Button(root,text="Show",command=showname)
b2=Button(root,text="Quit",command=fnquit)
l3=Label(root,text="You Typed")
e3=Entry(root)

l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
l3.grid(row=2,column=0)
e3.grid(row=2,column=1)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1,sticky=E)

root.mainloop()