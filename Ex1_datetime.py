"""Question 1: Create a program that asks the user to enter their name and age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year """

import datetime as dt
name = input("Enter your name: ")
age = int(input("Enter your age: "))

today = dt.date.today()
current_year = today.year

age100 = current_year + (100 - age)

print(f"{name}! you'll turn 100 in {age100} years.")

message_print = int(input(f"Enter the number of times you want to print this message: "))

for i in range(message_print):
    print(f"{name}! you'll turn 100 in {age100} years.")
