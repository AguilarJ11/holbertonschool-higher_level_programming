#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in text:
        last_space = False
        if c == '.' or c == ':' or c == '?':
            print(c)
            print()
            print()
            last_space = True
        elif last_space == True :
            continue
        else:
            print(c, end="")
