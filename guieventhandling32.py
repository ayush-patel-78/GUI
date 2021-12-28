from tkinter import * 
from tkinter import simpledialog,messagebox

def show_item():
    index=lb1.curselection()
    print(index)
root=Tk()
root.geometry("300x300")
l1=Label(root,text="Your selected text will appear here")
b1=Button(root,text="Show item",command=show_item)
lb1=Listbox(root,selectmode=MULTIPLE)  # types of modes are 1. (default) single , 2. MULTIPLE , 3. Browse , 4. EXTENDED 
sports=["Cricket","Hockey","Football","Badminton","Volleyball","Tennis","Rugby","Snooker","Wrestling","Basketball"]
for x in sports :
    lb1.insert(END,x)
lb1.grid(row=0,column=0,sticky=W)
b1.grid(row=1,column=0,sticky=W)
l1.grid(row=2,column=0,sticky=W)
root.mainloop() 