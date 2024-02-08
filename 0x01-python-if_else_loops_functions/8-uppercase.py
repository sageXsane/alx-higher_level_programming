#!/usr/bin/python3
def uppercase(string):
    for i in string:
        code = ord(i)
        if ((code >= 97) and (code < 123)):
            code = code - 32
        print("{}".format(chr(code)), end="")
    print(end="\n")