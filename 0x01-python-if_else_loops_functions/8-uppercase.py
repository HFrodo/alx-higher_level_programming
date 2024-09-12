#!/usr/bin/python3
def uppercase(s):
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            result.append(chr(ord(char) - 32))
        else:
            result.append(char)
    print(''.join(result))
