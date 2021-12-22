from tkinter import *
count=0
root=Tk()
root.geometry("200x200")
def increment():
    global count
    count=count+1
    l1.config(text=str(count))
    l1.pack()
l1=Label(root,text="0")

b1=Button(root,text="click me",command=increment)
b1.pack()
l1.pack()
root.mainloop()

