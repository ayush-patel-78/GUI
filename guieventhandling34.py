from tkinter import * 
from tkinter import simpledialog,messagebox

def show_item(e):
    index_tuple=lb1.curselection()
    str="\n"
    for i in index_tuple:
          str+=lb1.get(i)+"\n"
    l1.config(text="You selected:"+str)

root=Tk()
root.geometry("300x300")
l1=Label(root,text="Your selected text will appear here")

lb1=Listbox(root,selectmode=MULTIPLE)
sports=["Cricket","Hockey","Football","Badminton","Volleyball","Tennis","Rugby","Snooker","Wrestling","Basketball"]
for x in sports :
    lb1.insert(END,x)
lb1.bind("<<ListboxSelect>>",show_item)
lb1.grid(row=0,column=0,sticky=W)
l1.grid(row=2,column=0,sticky=W)
root.mainloop() 