# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:48:56 2020

@author: aditipc

Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""
def generate(num):
    dict1 = {}
    for i in range(1, num+1):
        dict1[i] = i*i
    return dict1

num = int(input("Enter the input Number: "))
print(generate(num))
