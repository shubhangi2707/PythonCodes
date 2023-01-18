"""Question 3: Take a list and prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

Extras:

1. Instead of printing elements one by one, make a new list that has all the elements less than 5 from this list
and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller
than that number given by the user.
"""

# Takes a list and prints out all elements that are less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in a:
    if element < 5:
        print(element)

# Extra 1: Makes a new list with all elements less than 5
less_than_five = []

for element in a:
    if element < 5:
        less_than_five.append(element)

print(less_than_five)

# Extra 2: Above code in one line (list comprehension)
print([element for element in a if element < 5])

# Extra 3: Returns a new list with elements from original list 'a' that are less than input number
new_list = []
num = int(input("Enter a number: "))
for element in a:
    if element < num:
        new_list.append(element)

print(new_list)
