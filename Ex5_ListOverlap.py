"""Take two lists:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
write a program that returns a list that contains elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:
1. Randomly generate two lists to test this
2. Write this in one line of Python. """


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in a:
    if i in b :
        c.append(i)
print(list(set(c)))

# Extra 1: randomly generating numbers of list using intersection
import random
a = random.sample(range(1, 50), 10)
b = random.sample(range(1, 50), 15)

print(list(set(a).intersection(set(b))))

# Extra 2: list comprehension
print(list(set([item for item in a if item in b])))
