#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":

    arg = len(argv)
    total = 0
    if arg > 0:
        for i in argv[1:]:
            total += int(i)
print("{}".format(total))
