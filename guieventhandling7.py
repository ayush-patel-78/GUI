from tkinter import *

    
root=Tk()
root.geometry("275x200")
l1=Label(root,bg="white",width=20,height=4)

b1=Button(root,text="Red",command=lambda:l1.config(bg="red"),width=4)

b2=Button(root,text="Green",command=lambda:l1.config(bg="green"),width=4)

b3=Button(root,text="Blue",command=lambda:l1.config(bg="blue"),width=4)
l1.grid(row=0,column=1,columnspan=3)
b1.grid(row=1,column=0)
b2.grid(row=1,column=2)
b3.grid(row=1,column=4)
root.mainloop()