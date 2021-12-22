from tkinter import *
root=Tk()
root.geometry("200x200")
defaultcolor=(root["bg"])
root.bind("<Return>",lambda e:root.config(bg="red"))
root.bind("<Escape>",lambda e: root.config(bg=defaultcolor))
root.mainloop()