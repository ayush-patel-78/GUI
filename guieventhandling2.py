from tkinter import * 
def showlbl():
    #l1=Label(root,text="Hello user")   # new label will be created every time we will click a button 
    l1.config(text="welcome to python")
    l1.pack()
root=Tk()
root.geometry("200x200")

b1=Button(root,text="Click me",command=showlbl)
b1.pack()
l1=Label(root)
l1.pack()

root.mainloop()
