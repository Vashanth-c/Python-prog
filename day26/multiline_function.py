from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("my window")
def get_data():
    t.delete(0.0,END)
    f=open("D:\\python program\\day26\\hello.txt","r")
    data=f.read()
    t.insert(0.0,data)
    f.close()
def write_data():
    f=open("D:\\python program\\day26\\hello.txt","w")
    f.write(t.get(0.0,END))
    f.flush()
    f.close()

t=Text(root,width=25,height=5)
t.pack()
b=Button(root,text="read",command=get_data)
b.pack()
b1=Button(root,text="write",command=write_data)
b1.pack()
root.mainloop()
