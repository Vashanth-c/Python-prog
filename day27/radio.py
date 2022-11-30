from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
def gen_check():
    print(v.get())
v=StringVar()
gen1=Radiobutton(root,text="male",variable=v,value="male",command=gen_check)
gen1.pack()
gen2=Radiobutton(root,text="female",variable=v,value="female")
gen2.pack()
b=Button(root,text="click",command=gen_check)
b.pack()
root.mainloop()
