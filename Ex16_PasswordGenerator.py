"""Ques 16: Write a password generator in Python. Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be 
random, generating a new password every time the user asks for a new password. 

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""

import random 
import string

def passwordgenerator():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    specialchar = "!@$&"
    number = string.digits
    valid_char_list = upper + lower + specialchar + number
    hardpsd = ""
    
    for i in range(12):
        a = random.choice(valid_char_list)
        hardpsd = hardpsd + a
    return hardpsd

weakpsd_list = ["California", "Australia", "Newzealand", "Florida", "Qwerty", "Password", "Washington", "Newdelhi"]


user_input = input('''What type of password you want?
1. Weak(W)
2. Medium(M)
3. Hard(H):
''').upper()

if user_input == "W":
    weakpsd = random.choice(weakpsd_list)
    print(f"Your password is: {weakpsd}")
    
elif user_input == "M":
    weakpsd = random.choice(weakpsd_list)
    random_num = random.sample(range(1000,9999),1)[0]
    print(f"Your password is: {weakpsd}{random_num}")
    
elif user_input == "H":
    print(f"Your password is: {passwordgenerator()}")
    
else:
    print("Invalid input!")
