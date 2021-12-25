from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
def showopen():
    fnames=filedialog.askopenfilenames(initialdir="e:/",title="Select a song",filetypes=[("mp3 files","*.mp3")])
    if fnames=="":
        messagebox.showinfo("No selection","u did not select any file")
    else :
        for i in fnames:
            lbl1=Label(root,text=i)
            lbl1.pack()
root=Tk()
root.geometry("600x300")
btn=Button(root,text="Open Files",command=showopen)
lbl1=Label(root,text="Your selected file names will appear here")

btn.pack()
lbl1.pack()
root.mainloop()