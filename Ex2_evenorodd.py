"""
Question 2: Ask the user for a number. Depending on whether the number is even or odd, print an appropriatenmessage to the user. 
Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

#check whether number is odd/even

number = int(input("Enter the number:"))

if number%2 == 0:
    print(f"{number} is even!")
    
else:
    print(f"{number} is odd!")
    
# Extra number 1

number1 = int(input("Enter another number:"))

if number%4 == 0:
    print(f"{number} is even and divisible by 4!")
    
else:
    print(f"{number} is not divisible by 4!")
    
# Extra number 2

num = int(input("Enter number to check: "))
check = int(input("Enter number to divide by: "))

if num % check == 0:
    print(f'{check} divides evenly into {num} and the quotient is {num/check}')
else:
    print(f"{check} does not divide evenly into {num}")
