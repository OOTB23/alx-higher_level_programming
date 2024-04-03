#!/usr/bin/python3def safe_print_list(my_list=[], x=0):
def safe_print_list(my_list=[], x=0):
    try:
        key = 0
        while key < x :  
            print(my_list[key] , end ="")
            key = key +1
        print("")
        return key
    except IndexError:
        print("")
        return key
