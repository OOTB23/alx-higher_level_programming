#!/usr/bin/python3def safe_print_list(my_list=[], x=0):
    try:
        key = 0
        while key < x :  
            print(my_list[key] , end ="")
            key = key +1
        return key
    except IndexError:
        return key
    
new_list = safe_print_list([1,2,3,4,5],5)
print ("\n",new_list,sep="")

