from tkinter import * 
from tkinter import simpledialog,messagebox

def show_item():
    index_tuple=lb1.curselection()
    if len(index_tuple)==0:
        messagebox.showerror("No Selection","Please select an item")
    else:
        str="\n"
        for i in index_tuple:
            str+=lb1.get(i)+"\n"
        l1.config(text="You selected:"+str)

root=Tk()
root.geometry("300x300")
l1=Label(root,text="Your selected text will appear here")
b1=Button(root,text="Show item",command=show_item)
lb1=Listbox(root,selectmode=MULTIPLE)
sports=["Cricket","Hockey","Football","Badminton","Volleyball","Tennis","Rugby","Snooker","Wrestling","Basketball"]
for x in sports :
    lb1.insert(END,x)
lb1.grid(row=0,column=0,sticky=W)
b1.grid(row=1,column=0,sticky=W)
l1.grid(row=2,column=0,sticky=W)
root.mainloop() 