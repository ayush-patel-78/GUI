from tkinter import * 
def showlbl():
    l1=Label(root,text="Hello user")
    l1.pack()
root=Tk()
root.geometry("200x200")
b1=Button(root,text="Click me",command=showlbl)
b1.pack()
root.mainloop()
