import tkinter
root=tkinter.Tk()
root.geometry("400x400")
lbl1=tkinter.Label(root,text="This is label 1",bg="red",fg="white",width=10)
lbl2=tkinter.Label(root,text="label 2",bg="blue",fg="white",width=10)
lbl3=tkinter.Label(root,text="label 3",bg="green",fg="white",width=10)
lbl4=tkinter.Label(root,text="label 4",bg="yellow",fg="black",width=10)
lbl1.grid(row=0,column=0)
lbl2.grid(row=0,column=1)
# lbl3.grid(row=1,column=0) # if we dont provide sticky argument then label 3 will not expand/stretch in column 0 
lbl3.grid(row=1,column=0,sticky=tkinter.E+tkinter.W) # sticky arg will stretch label 3 in full column 
lbl4.grid(row=1,column=1)
root.mainloop()