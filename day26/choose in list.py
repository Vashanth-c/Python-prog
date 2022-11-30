from tkinter import *
master=Tk()
Listbox=Listbox(master)
Listbox.pack()
for item in ["one","two","three","four"]:
    Listbox.insert(END,item)
def select():
    print(Listbox.get(Listbox.curselection()))

b=Button(master,text="choose",command=select)
b.pack()
mainloop()
