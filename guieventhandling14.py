from tkinter import *
import sys
def showname():
    # 1st way 
    # fname=e1.get()
    # lname=e2.get()
    # l3.config(text=fname+" "+lname)

    #2nd way 
    name=e1.get()+" "+e2.get()
    l3.config(text=name)
def fnquit():
    # sys.exit(0)  # this will kill the whole code 
    root.destroy() # this will only destroy root window if there is another window then that will not be destroyed 
root=Tk()
root.geometry("250x200")
l1=Label(root,text="First Name:")
l2=Label(root,text="Last Name:")
e1=Entry(root)
e2=Entry(root)
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

print("Hue hue hue hue hue ")