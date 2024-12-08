#!/usr/bin/python3
'''
a function that divides element by element 2 lists
'''


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            result = num1 / num2
        except (TypeError):
            print("wrong type")
        except (ZeroDivisionError):
            print("division by 0")
        except (IndexError):
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
