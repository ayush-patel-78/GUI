import tkinter
import tkinter.font as tkFont
root=tkinter.Tk()
root.geometry("600x400")
myFont=tkFont.Font(size=22)
mylabel=tkinter.Label(root,text="Hello \nWorld",font=myFont,width=20,borderwidth=2,height=4,relief="solid")
mylabel.config(anchor="s")  # anchor attribute is used for direction where text should appear inside label 
mylabel.pack()
root.mainloop()