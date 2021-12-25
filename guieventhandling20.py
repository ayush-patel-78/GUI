from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
def showopen():
    fname=filedialog.askopenfilename(initialdir="d:/",title="Select a song",filetypes=[("mp3 files","*.mp3")])
    if fname!="":
        messagebox.showinfo("You selected:",fname)
    else:
        messagebox.showinfo("No selection","u did not select any file")
root=Tk()
root.geometry("200x200")
btn=Button(root,text="Open File",command=showopen)
btn.pack()
root.mainloop()