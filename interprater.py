import io
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



## tokenize
#tokens = code.split()
#line = " ".join(tokens)


c_code = open("main.c", 'w', encoding='utf-8')
c_code.write(code)
c_code.close()

