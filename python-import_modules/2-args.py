#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    if arg == 1:
        print("{} argument".format(arg))
        print("{}: {}".format(arg, sys.argv[1]))
    else:
        print("{} arguments".format(arg))
        for i in range(1, arg):
            print("{}: {}".format(i, sys.argv[i]))