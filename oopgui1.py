from tkinter import *
class MyFirstGUI:
    def __init__(self,root) :
        self.root=root
        self.root.title("Hue hue hue...")
        self.root.geometry("300x300")
        self.mylabel=Label(self.root,text="Click the button")
        self.mylabel.pack()
        self.closebutton=Button(self.root,text="Close",command=self.root.destroy)
        self.closebutton.pack()
        self.greetbutton=Button(self.root,text="Greet",command=self.greet)
        self.greetbutton.pack()
 
    def greet(self):
        self.mylabel.config(text="Hehe u r fucked ")

root=Tk()
mygui=MyFirstGUI(root)
root.mainloop()