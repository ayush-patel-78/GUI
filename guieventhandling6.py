from tkinter import *
def red():
    l1.config(bg="red")
    
def green():
    l1.config(bg="green")
    
def blue():
    l1.config(bg="blue")
    
root=Tk()
root.geometry("275x200")
l1=Label(root,bg="white",width=20,height=4)

b1=Button(root,text="Red",command=red)

b2=Button(root,text="Green",command=green)

b3=Button(root,text="Blue",command=blue)
l1.grid(row=0,column=1,columnspan=3)
b1.grid(row=1,column=0)
b2.grid(row=1,column=2)
b3.grid(row=1,column=4)
root.mainloop()