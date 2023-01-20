"""Ques 9: Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

1. Keep the game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when the game ends, print this out."""

import random
a = random.sample(range(1, 10),1)[0]

user_input = int(input("Enter your guess:"))

if user_input == a:
    print("Bingo! You guessed the right number.")
    
elif user_input > a:
    print("Too high!")

else:
    print("Too low!")
    
print(f"The actual number was {a}")

# Extra 1

a = random.sample(range(1, 10),1)[0]

while True:
    
    user_input = int(input("Enter your guess:"))

    if user_input == a:
        print("Bingo! You guessed the right number.")
        break

    elif user_input > a:
        print("Too high!")

    else:
        print("Too low!")

    msg = input("Do you want to continue? ").lower()
    
    if msg == "no" or msg == "n":
        break
    elif msg == "yes" or msg == "y":
        continue
    else:
        print("Invalid answer")
           
print(f"The actual number was {a}")

# Extra 2

counter = 0

while True:
    
    user_input = int(input("Enter your guess:"))

    if user_input == a:
        print("Bingo! You guessed the right number.")
        break

    elif user_input > a:
        print("Too high!")

    else:
        print("Too low!")

    msg = input("Do you want to continue? ").lower()
    
    counter = counter + 1
    
    if msg == "no" or msg == "n":
        break
    elif msg == "yes" or msg == "y":
        continue   
    else:
        print("Invalid answer")    
    
print(f"The actual number was {a} and you took {counter} turns.")
