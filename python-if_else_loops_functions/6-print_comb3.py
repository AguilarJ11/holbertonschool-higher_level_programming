#!/usr/bin/python3
for n in range(1, 100):
    if int(str(n)[-1]) == 0:
        continue
    elif int(str(n)[-1]) == int(str(n)[0]) and n > 9:
        continue
    elif int(str(n)[0]) > int(str(n)[-1]) and n > 9:
        continue
    elif n == 89:
        print("{:02d}".format(n), end='\n')
    else:
        print("{:02d}".format(n), end=', ')
