#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
arg = len(argv)
for i in range(1, arg + 1):
    sum = sum + int(argv[i])
print(sum)