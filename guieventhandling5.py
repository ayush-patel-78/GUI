from tkinter import *

root=Tk()

root.geometry("200x200")
def increment():
    # count=obj.get()
    # count=count+1
    # obj.set(count)

    # we can do this in one line 
    obj.set(obj.get()+1)
    
obj=IntVar()
l1=Label(root,textvar=obj)

b1=Button(root,text="click me",command=increment)
b1.pack()
l1.pack()
root.mainloop()