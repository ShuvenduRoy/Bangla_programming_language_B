import io
import os
import time

def generate_c():
    bangla_code = io.open("main.b", mode="r", encoding="utf-8")
    code = bangla_code.read()

    code = "#include <stdio.h>\n\
    FILE *fp;\n" + code

    keywords = {
            "প্রধান":"main",
            "দেখাও(":"fprintf(fp, ",
            "ফাকা": "void"
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

    c_code = open("main.c", 'w', encoding='utf-8')
    c_code.write(code)
    c_code.close()

    os.system('gcc main.c -o main')
    time.sleep(.1)
    os.system('.\main.exe')
