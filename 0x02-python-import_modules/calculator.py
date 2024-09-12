#!/usr/bin/python3
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    result = a/b
    if b == 0:
        raise ZeroDivisionError("Cannnot divide by zero")
    else:
        return result

def multiply(a,b):
    return a*b

if __name__== "__main__":
    print("This module contains basic calculator functions.")

"""
    print(f"3 + 5 = {add(3, 5)}")
    print(f"16 * 356 = {multiply(16, 356)}")
    print(f"8667 / 685 = {divide(8667, 685)}")
    print(f"5004 - 94356 = {subtract(5004, 94356)}")
"""
