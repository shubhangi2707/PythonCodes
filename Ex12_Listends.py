"""Ques 12: Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function."""

import random

def mylist(x):
    new_list = [a[0], a[len(a) - 1]]
    print(new_list)
    
a = random.sample(range(1,50),10)  
mylist(a)
print(f"Randomly generated numbers are: {a}")
