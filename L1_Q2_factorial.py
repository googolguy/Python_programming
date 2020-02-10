# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:36:09 2020

@author: aditipc

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
def factorial(num):
    if ((num == 0) or (num == 1)):
        return 1
    else:
        temp = 1
        while num > 0:
            temp = temp * num
            num = num-1
        return temp

num = int(input("Enter the number to calculate factorial: "))
print(factorial(num))

# Using recursion to solve the above problem
# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num-1)
