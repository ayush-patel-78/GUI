from tkinter import *
from tkinter import messagebox

def showgender():
    a=x.get()
    if a==1:
        messagebox.showinfo("Gender","You selected Male")
    else:
        messagebox.showinfo("Gender","You selected Female")
root=Tk()
root.geometry("200x200")
l1=Label(root,text="Select your gender")
x=IntVar()
rb1=Radiobutton(root,text="Male",command=showgender,variable=x,value=1)
rb2=Radiobutton(root,text="Female",command=showgender,variable=x,value=2)

l1.grid(row=0,column=0)
rb1.grid(row=1,column=0,sticky=W)
rb2.grid(row=2,column=0,sticky=W)

root.mainloop()

