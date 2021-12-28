from tkinter import *
from tkinter import messagebox

def showgender():
    messagebox.showinfo("Gender","You selected "+x.get())
root=Tk()
root.geometry("200x200")
l1=Label(root,text="Select your gender")
x=StringVar()
rb1=Radiobutton(root,text="Male",command=showgender,variable=x,value="Male")
rb2=Radiobutton(root,text="Female",command=showgender,variable=x,value="Female")
l1.grid(row=0,column=0)
rb1.grid(row=1,column=0,sticky=W)
rb2.grid(row=2,column=0,sticky=W)

root.mainloop()

