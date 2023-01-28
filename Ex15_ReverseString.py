"""Ques 15: Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. """

def reverse_string(str1):
    revstr = str1[::-1]
    return revstr

org_string = input("Enter the string you want to reverse: ")
print(f"Reversed string is {reverse_string(org_string)}")
