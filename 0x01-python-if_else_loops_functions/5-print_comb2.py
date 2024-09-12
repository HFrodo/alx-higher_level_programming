#!/usr/bin/python3
for i in range(100):
    if i == 99:
        break
    print("{0:02d}, ".format(i), end="")
print("{:d}".format(99))
