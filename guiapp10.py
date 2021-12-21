import tkinter
root=tkinter.Tk()
root.geometry("600x400")
strobj=tkinter.StringVar()
lbl=tkinter.Label(root,borderwidth=2,relief="solid",textvariable=strobj)
lbl.pack()
strobj.set("hello world")
root.mainloop()