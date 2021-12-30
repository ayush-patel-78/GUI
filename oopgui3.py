from tkinter import *
from tkinter import messagebox,simpledialog
class MyGUI:
    def __init__(self,root):
        self.root=root
        root.geometry("400x200+100+200")
        self.l1=Label(root,text="Number Division Program",font="Arial 18 bold")
        self.l2=Label(root,text="First No:")
        self.l3=Label(root,text="Second No:")
        self.l4=Label(root,text="Second No:")
        self.l4=Label(root,text="Result:")
        self.e1=Entry(root)
        self.e2=Entry(root)
        self.e3=Entry(root,fg="green")
        self.e1.bind("<Return>",lambda e:self.e2.focus())
        self.b1=Button(root,text="Divide",command=self.divide)
        self.b2=Button(root,text="Clear",command=self.clear)
        self.b3=Button(root,text="Quit",command=self.finish)
        self.l1.grid(row=0,column=0,columnspan=4)
        self.l2.grid(row=1,column=0,sticky=E)
        self.e1.grid(row=1,column=1)
        self.l3.grid(row=2,column=0,sticky=E)
        self.e2.grid(row=2,column=1)
        self.l4.grid(row=3,column=0,sticky=E)
        self.e3.grid(row=3,column=1)
        self.b1.grid(row=4,column=0,pady=5,padx=5,sticky=E+W)
        self.b2.grid(row=4,column=1,pady=5,padx=5,sticky=E+W)
        self.b3.grid(row=4,column=2,pady=5,padx=5,sticky=E+W)
    def clear(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e1.focus()
        

    def divide(self):
        try:
            self.e3.delete(0,END)
            a=int(self.e1.get())
            b=int(self.e2.get())
            c=a/b
            self.e3.insert(0,str(c))
        except ZeroDivisionError:
            messagebox.showerror("Arithmetic error!","Denominator should not be 0") 
        except ValueError:
            messagebox.showerror("Invalid input!","only digits allowed")
            

    def finish(self):
        answer=messagebox.askyesno("Quitting","Are u sure ?")
        if answer==True:
            name=simpledialog.askstring("Quiting","What's ur name ?")
        if name is None or name=="":
            name="Bro"
        messagebox.showinfo("Thank You ","Have a good day,"+name)
        self.root.destroy()
root=Tk()
mygui=MyGUI(root)
root.mainloop()