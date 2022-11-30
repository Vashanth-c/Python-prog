from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
def deg_check():
    if c1.get()==1:
        print("B.E")
    if c2.get()==1:
        print("M.E")
c1=IntVar()
c2=IntVar()
deg1=Checkbutton(root,text="U.G",variable=c1,command=deg_check)
deg1.pack()
deg2=Checkbutton(root,text="P.G",variable=c2,command=deg_check)
deg2.pack()
root.mainloop
