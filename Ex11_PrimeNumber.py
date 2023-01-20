""" Ques 11: Ask the user for a number and determine whether the number is prime or not. """

def prime_no(num):
    flag = True
    
    if num == 1:
        print("Entered number is not prime!")
    elif num == 2:
        print("Entered number is prime!")
    elif num == 0:
        print("Entered number is not prime!")
    else:
        for i in range(2,num):
            if(num % i == 0):
                print("Entered number is not prime!")
                flag = False
                break
                
        if flag == True:
            print("Entered number is prime!")
                
num = int(input("Enter a number you want to check is prime or not: "))
prime_no(num)
