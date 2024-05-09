#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
arg = len(argv)
total = 0
if arg > 0:
    for i in range(1, arg + 1):
        total += int(argv[i])
print(total)