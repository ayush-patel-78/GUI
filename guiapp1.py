import tkinter
root=tkinter.Tk()
root.title("My gui app")
root.geometry("400x400+200+300")
img=tkinter.PhotoImage(file="D:/NEOS/assets/circuitry 1.png")
root.iconphoto(root,img)
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
width=w//2
height=h//2
x=w//4
y=h//4
# root.geometry(str(width)+"x"+str(height)+"+"+str(x)+"+"+str(y))
root.geometry(f"{width}x{height}+{x}+{y}")
root.resizable(False,False) # size change nhi kar sakta user 1st arg used for can we change width , 2nd arg used for can we change heighht 
root.mainloop()