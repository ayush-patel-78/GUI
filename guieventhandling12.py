from tkinter import *

# 1st way to change the color of root window using lambda function or using basic functions 
# of python but for this either we have to write 3 lamdas or 3 functions to change the color,
# we can do it in more simpler way as given in guieventhandling13.py

root=Tk()
root.geometry("200x200+100+200")
root.bind("r",lambda e:root.config(bg="red"))
root.bind("g",lambda e:root.config(bg="green"))
root.bind("b",lambda e:root.config(bg="blue"))
root.mainloop()
