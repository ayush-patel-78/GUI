from tkinter import * 
from tkinter import simpledialog,messagebox

def show_item():
    pos=simpledialog.askinteger("Input","Enter the pos of item",minvalue=1,maxvalue=lb1.size())
    if type(pos) is int:
        item=lb1.get(pos-1)
        l1.config(text="You selected:"+item)
    else:
        l1.config(text="You did not any position")
root=Tk()
root.geometry("300x300")
l1=Label(root,text="Your selected text will appear here")
b1=Button(root,text="Show item",command=show_item)
lb1=Listbox(root)
sports=["Cricket","Hockey","Football","Badminton","Volleyball","Tennis","Rugby","Snooker","Wrestling","Basketball"]
for x in sports :
    lb1.insert(END,x)
lb1.grid(row=0,column=0,sticky=W)
b1.grid(row=1,column=0,sticky=W)
l1.grid(row=2,column=0,sticky=W)
root.mainloop() 