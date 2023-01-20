"""Ques 13: Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Make sure to ask the user to enter the number of sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)"""


def fibonacciseq(fib_len):
    fib_list = [0,1] 
    if fib_len == 0:
        return []
    elif fib_len == 1:
        return [1]
    else:
        for i in range(fib_len - 2):
            fib_list.append(fib_list[i] + fib_list[i+1])
        return fib_list
            
fib_len = int(input("Enter the length of Fibonnaci sequence you want to generate: "))          
flst = fibonacciseq(fib_len)
print(f"The fibonacci sequence is: {flst}" )
