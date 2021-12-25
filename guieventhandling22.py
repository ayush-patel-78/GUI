from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
def showopen():
    # 2nd way to handle tuple and string  
    fnames=filedialog.askopenfilenames(initialdir="e:/",title="Select a song",filetypes=[("mp3 files","*.mp3")])
    if type(fnames) is tuple:
        str =""
        for songname in fnames:
            str+=songname+"\n"
        lbl.config(text=str)
    else:
        messagebox.showinfo("No selection","u did not select any file")
    
root=Tk()
root.geometry("600x300")
btn=Button(root,text="Open Files",command=showopen)
lbl=Label(root,text="Your selected file names will appear here")

btn.pack()
lbl.pack()
root.mainloop()