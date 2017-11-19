from interprater import generate_c
from tkinter import *

def donothing():
   # filewin = Toplevel(root)
   # button = Button(filewin, text="Do nothing button")
   # button.pack()
   pass

def build():
    raw_code = code.get('1.0', END)

    b_code = open("main.b", 'w', encoding='utf-8')
    b_code.write(raw_code)
    b_code.close()
    print("build successful")

    generate_c()

root = Tk()
root.title("B Programming environment")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)

# Build menu
build_menu = Menu(menubar, tearoff=0)
build_menu.add_cascade(label="Build", command=build)
build_menu.add_cascade(label="Run")
menubar.add_cascade(label="Build", menu = build_menu)

# help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# Text box menu
code = Text(root)
code.pack()

output = Text(root, height=10)
output.insert(END, "Output: ")
output.pack()
# code.insert(END, "first line")

root.mainloop()
