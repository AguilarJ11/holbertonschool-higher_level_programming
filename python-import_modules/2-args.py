#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = len(argv) - 1
    if arg == 1:
        print("{} argument".format(arg))
        print("{}: {}".format(arg, argv[1]))
    else:
        print("{} arguments".format(arg))
        for i in range(1, arg):
            print("{}: {}".format(i, argv[i]))