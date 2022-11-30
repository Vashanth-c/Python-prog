from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
def button_click():
    root1=Tk()
    root1.geometry("400x400")
    root1.title("My Window")
b=Button(root,text="Click Here!",command=button_click,bg="#FFF323")
b.pack()
root.mainloop()
    
