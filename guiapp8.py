import tkinter
from tkinter.font import Font
root=tkinter.Tk()
lbl=tkinter.Label(root,text="Welcome", font="Arial 22 bold",bg="blue",fg="white")
lbl.pack()
# print(lbl.keys())           #label stores properties or attributes in dictionary in key value pairs , every widget contains a dictionary 
print(lbl['font'])            # we can see the values of key using subscript operator 
lbl['text']="Good Evening"    # we can also manipulate the values of key since dictionary is mutable 
lbl['bg']='red'
root.mainloop()