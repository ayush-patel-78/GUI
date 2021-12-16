import tkinter
import tkinter.font as tkFont
root = tkinter.Tk()
root.geometry("600x200")
myFont=tkFont.Font(weight="bold",family="helvetica")
mylabel= tkinter.Label(root,text="Welcome to python ",font=myFont)
mylabel.pack()
root.mainloop()