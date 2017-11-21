from interprater import generate_c
from tkinter import *
import io
import os
import re

def donothing():
   # filewin = Toplevel(root)
   # button = Button(filewin, text="Do nothing button")
   # button.pack()
   pass

def highlight():
    code.tag_configure("highlight", foreground="green")
    # code.tag_add("highlight", "3.0", "3.5")

    raw = code.get('1.0', END)
    raw = raw.split('\n')

    p = re.compile("প্রধান|দেখাও|গ্রহন|ফাকা|দশমিক|সংখ্যা|বর্ণ|%ব|%স|%দ|%চ|%চ|যতখন|কর|জন্য|যদি|থাম|৳|$")

    for i in range(len(raw)):
        for m in p.finditer(raw[i]):
            if len(m.group()) > 0:
                start = str(i+1)+'.'+str(m.start())
                end = str(i+1)+'.'+str(m.start() + len(m.group()))
                code.tag_add("highlight", start, end)
                # print(start, end)
            # print (i, m.start(), m.group(), len(m.group()))



def convert_number(code):
    keywords = {
            "0":"০",
            "1":"১",
            "2":"২",
            "3":"৩",
            "4":"৪",
            "5":"৫",
            "6":"৬",
            "7":"৭",
            "8":"৮",
            "9":"৯"
            }

    # converting keywords into c
    key_word_keys = list(keywords.keys())
    for i in range(len(keywords.keys())):
        code = code.replace(key_word_keys[i], keywords[key_word_keys[i]])

    return code

def build():
    raw_code = code.get('1.0', END)

    b_code = open("main.b", 'w', encoding='utf-8')
    b_code.write(raw_code)
    b_code.close()
    print("build successful")

    generate_c()

def run():
    # os.startfile('.\main.exe')

    output_file = io.open("output.txt", mode="r", encoding="utf-8")
    result = output_file.read()
    result = convert_number(result)

    output.delete('1.0', END)

    output.insert(END, "Output: \n")
    output.insert(END, result)

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
editmenu.add_command(label="Highlight", command=highlight)

editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)

# Build menu
build_menu = Menu(menubar, tearoff=0)
build_menu.add_cascade(label="Build", command=build)
build_menu.add_cascade(label="Run", command=run)
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
