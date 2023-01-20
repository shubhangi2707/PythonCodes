# Ques 4: Create a program that asks the user for a number and prints out a list of all the divisors of that number.

number = int(input("Enter the number: "))
new_list = []

for i in range(1,number + 1):
    if number % i == 0:
        new_list.append(i)
        
print(f'Divisors of {number} are: {new_list}')

# list comprehension

print([i for i in range(1,number + 1) if number % i == 0])
