from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
v=StringVar()
def get_label():
    print(v.get())
def set_label():
    v.set("Welcome to Python")
b=Button(root,text="get",command=get_label,bg="red")
b.pack()
b1=Button(root,text="set",command=set_label,bg="red")
b1.pack()
l=Label(root,textvariable=v,bg="red",fg="white")
v.set("Hello World")
l.pack()
root.mainloop()
