"""Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)"""

def palindrome(s):
    return string == string[::-1]

string = str(input("Enter the sentence: "))
string = string.lower()

if palindrome(string):
    print(f"\'{string}\' is Palindrome.")
else:
    print(f"\'{string}\' is not Palindrome.")

# list comprehension
print("palindrome") if string == string[::-1] else print("not palindrome")
