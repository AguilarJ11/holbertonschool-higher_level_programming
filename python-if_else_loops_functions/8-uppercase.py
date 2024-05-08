#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            print("{}".format(chr(ord(i) - 32)), end="")
    print("")
