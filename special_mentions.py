# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:04:37 2020

@author: aditipc

Description: Problems that can be solved using imports.
"""

"""
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""
# userin = [i for i in input("Enter the Input sequence: ")]
# digit = 0
# letter = 0
# for item in userin:
#     if item.isdigit():
#         digit += 1
#     elif item.isalpha():
#         letter += 1

# print("LETTERS ", letter, "\nDIGITS ", digit)


"""
Question: 
Write a program which accepts a sequence of comma separated 4 digit binary 
numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
"""
# userin = input("Enter comma seperated binary numbers: ").split(",")
# temp = []
# for item in userin:
#     i = int(item, 2)
#     if i%5 == 0:
#         temp.append(item)

# print(",".join(temp))


"""
Question:
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
write a program to make a list whose elements are intersection of the above given lists.
"""
# l1 = [1,3,6,78,35,55]
# l2 = [12,24,35,24,88,120,155]
# s1 = set(l1)
# s2 = set(l2)

# s1 &= s2
# print(list(s1))


"""
Question:
Please write a program to shuffle and print the list [3,6,7,8].
"""
# from random import shuffle
# l1 = [3,6,7,8]
# shuffle(l1)
# print(l1)