from tkinter import *
def red():
    # l1.config(bg="red")   #1st way 
    l1["bg"]="red"          #using key value pair
    
def green():
    # l1.config(bg="green")  #1st way
    l1["bg"]="green"         # using key value pair
    
def blue():
    # l1.config(bg="blue")   #1st way
    l1["bg"]="blue"          #using key value pair
    
root=Tk()
root.geometry("275x200")
l1=Label(root,bg="white",width=20,height=4)

b1=Button(root,text="Red",command=red,width=4)

b2=Button(root,text="Green",command=green,width=4)

b3=Button(root,text="Blue",command=blue,width=4)
l1.grid(row=0,column=1,columnspan=3)
b1.grid(row=1,column=0)
b2.grid(row=1,column=2)
b3.grid(row=1,column=4)
root.mainloop()