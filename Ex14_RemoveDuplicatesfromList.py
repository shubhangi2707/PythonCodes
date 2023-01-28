"""Ques 14: Write a program (function) that takes a list and returns a new list that contains all the elements 
of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets."""

import random

def checkduplicatelist(list_a):
    listlen = len(list_a)
    list_b = []
    for i in range(0,listlen):
        if list_a[i] in list_b:
            continue
        else:
            list_b.append(list_a[i])
    return list_b
        
list_a = [random.randint(1,15) for i in range (20)]
list_b = checkduplicatelist(list_a)

print(f"Elements of list without duplicates are: {list_b}")

# Extra: converting list into set

def remove_duplicate(list_a):
    list_b = list(set(list_a))
    return list_b
        
list_a = [random.randint(1,15) for i in range (20)]

print(list_a)
print(f"Elements of list without duplicates are: {remove_duplicate(list_a)}")
