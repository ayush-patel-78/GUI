import tkinter
root=tkinter.Tk()
root.geometry("600x200")
mylabel=tkinter.Label(root,text="Welcome to python")
mylabel.config(fg="blue",bg="red")
root.config(bg="yellow")
mylabel.pack()
root.mainloop()