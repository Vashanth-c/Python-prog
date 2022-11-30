from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("400x400")
root.title("ComboBox")
v=StringVar()
def select():
    print(v.get())
def store():
    v.set('sun')

days=ttk.Combobox(root,textvariable=v)
days['values']=('sun','mon','tue')
days.current(1)
days.pack()
sel=Button(root,text="select",command=select)
sel.pack()
store=Button(root,text="store",command=store)
store.pack()
root.mainloop()
