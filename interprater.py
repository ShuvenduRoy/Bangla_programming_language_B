import io
import os
import time
import re


def get_next_variable(variable):
    if 'variable_counter' not in globals():
        global variable_counter
        variable_counter = 0

    if 'variable_map' not in globals():
        global variable_map
        variable_map = {}

    var = ""
    for c in variable:
        if c is not ' ':
            var += c
    variables = var.split(',')

    for variable in variables:
        if '[' in variable:
            variable = re.match( r'.*\[', variable, re.M|re.I).group(0)[:-1]
        elif '=' in variable:
            variable = re.match( r'.*=', variable, re.M|re.I).group(0)[:-1]
        # print(variable)

        # removing the $
        variable = variable[1:]
        new_var = "var" + str(variable_counter)
        variable_counter += 1
        variable_map[variable] = new_var


def generate_c():

    bangla_code = io.open("main.b", mode="r", encoding="utf-8")
    code = bangla_code.read()

    code = "#include <stdio.h>\n\
    FILE *fp;\n" + code

    keywords = {
            "০":"0",
            "১":"1",
            "২":"2",
            "৩":"3",
            "৪":"4",
            "৫":"5",
            "৬":"6",
            "৭":"7",
            "৮":"8",
            "৯":"9",
            "প্রধান":"main",
            "দেখাও(":"fprintf(fp, ",
            "গ্রহন":"scanf",
            "ফাকা": "void",
            "দশমিক":"double",
            "সঙ্খা": "int",
            "বর্ণ" : "char",
            "%ব" : "%s",
            "%স" : "%d",
            "%দ" : "%lf",
            "%চ" : "%c",
            "\ন" : "\\n",
            "যতখন": "while",
            "কর": "do",
            "জন্য": "for",
            "যদি": "if",
            "থাম": "break",
            "৳":"$"
            }

    # converting keywords into c
    key_word_keys = list(keywords.keys())
    for i in range(len(keywords.keys())):
        code = code.replace(key_word_keys[i], keywords[key_word_keys[i]])


    # adding special lines for c
    new_code = ""
    for line in code.splitlines():
        new_code += (line + '\n')
        if 'main' in line:
            new_code += '    fp = fopen("output.txt", "w+");\n'
    code = new_code

#    m = re.search('int ', 'a=1, b[50], c=0')
#    src = 'a=1,b[50],c=0'
#    src = src.split(',')
#    re.match( r'.*=', src[0], re.M|re.I).group(0)[:-1]
#    re.split('=?[0-9]*,?', '', flags=re.IGNORECASE)
#    print(m.group(1))

    for line in code.splitlines():
        # remove all extra space with one space
        if line.startswith(' '):
            line = re.sub(' +', " ", line)
        # remove the first space
        if line.startswith(' '):
            line = line[1:-1]

        if 'int ' in line:
            get_next_variable(line[4:])
        elif 'float ' in line:
            get_next_variable(line[6:])
        elif 'char ' in line:
            get_next_variable(line[5:])
        elif 'double ' in line:
            get_next_variable(line[7:])

    # Replacing variable
    # converting keywords into c
    keywords = variable_map
    key_word_keys = list(keywords.keys())
    for i in range(len(keywords.keys())):
        code = code.replace('$'+key_word_keys[i], keywords[key_word_keys[i]])
        code = code.replace('&'+key_word_keys[i], '&'+keywords[key_word_keys[i]])


    # adding special lines for c
    new_code = ""
    for line in code.splitlines():
        new_code += (line + '\n')
        if 'main' in line:
            new_code += '    fp = fopen("output.txt", "w+");\n'
    code = new_code


    c_code = open("main.c", 'w', encoding='utf-8')
    c_code.write(code)
    c_code.close()

    os.system('gcc main.c -o main')
    time.sleep(.1)
    # os.system('.\main.exe')

generate_c()
