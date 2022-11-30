from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
def get_entry():
    print("Welcome:",e.get())
e=Entry(root)
e.insert(0,"Hello")
e.pack()
b=Button(root,text="get",command=get_entry,bg="red")
b.pack()
root.mainloop()
