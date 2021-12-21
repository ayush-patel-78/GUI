import tkinter
root=tkinter.Tk()
root.geometry("600x400")
img=tkinter.PhotoImage(file="d:/NEOS/assets/neoslogo.png")
lbl=tkinter.Label(root,text="Welcome to",image=img,compound=tkinter.RIGHT)
lbl.pack()
root.mainloop()
