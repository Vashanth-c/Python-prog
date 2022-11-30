from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("Menu Example")

def hello():
    print("New")
def openfile():
    print("opening a file")
menubar=Menu(root)

filemenu=Menu(menubar)
filemenu.add_command(label="New",command=hello)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_separator()
menubar.add_cascade(label="File",menu=filemenu)

submenu=Menu(filemenu)
submenu.add_command(label="One")
submenu.add_command(label="Exit",command=root.destroy)
filemenu.add_cascade(label="Recent",menu=submenu)
root.config(menu=menubar)
root.mainloop()
