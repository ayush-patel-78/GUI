import tkinter
root=tkinter.Tk()
root.geometry("400x400")
lbl1=tkinter.Label(root,text="label 1",bg="red",fg="white",width=10)
lbl2=tkinter.Label(root,text="label 2",bg="blue",fg="white",width=10)
lbl3=tkinter.Label(root,text="label 3",bg="green",fg="white",width=10)
lbl4=tkinter.Label(root,text="label 4",bg="yellow",fg="black",width=10)
lbl1.grid(row=0,column=0)
lbl2.grid(row=1,column=1)
lbl3.grid(row=2,column=2)
lbl4.grid(row=3,column=3)
root.mainloop()

