from tkinter import *
root=Tk()
root.geometry("200x200")
lb1=Listbox(root)
sports=["Cricket","Football","Hockey","Basketball","Volleyball","Tennis","Rugby","Badminton"]
for s in sports:
    lb1.insert(END,s)

print(lb1.get(0,2))    ## get method returns the list items present in the list box 
lb1.delete(0,2)        ## delete method deletes the items present between the index range 
lb1.grid(row=0,column=0,sticky=W)
root.mainloop()