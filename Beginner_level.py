# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:29:44 2020

@author: aditipc

Description: Beginner level questions based on Python
"""

"""
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
# def numbers():
#     temp = []
#     for i in range(2000,3201):
#         if ((i%7 == 0) and (i%5 != 0)):
#             temp.append(str(i))
#     return temp

# out = numbers()
# print(",".join(out))


"""
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
'''Solution: 1'''
# def factorial(num):
#     if ((num == 0) or (num == 1)):
#         return 1
#     else:
#         temp = 1
#         while num > 0:
#             temp = temp * num
#             num = num-1
#         return temp

# num = int(input("Enter the number to calculate factorial: "))
# print(factorial(num))

'''Solution: 2'''
# Using recursion to solve the above problem
# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num-1)


"""
Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""
# def generate(num):
#     dict1 = {}
#     for i in range(1, num+1):
#         dict1[i] = i*i
#     return dict1

# num = int(input("Enter the input Number: "))
# print(generate(num))


"""
Question:
Write a program which accepts a sequence of comma-separated numbers from console and 
generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""
# uinput = input("Enter a series of numbers seperated by comma: ")

# l1 = uinput.split(",")
# t1 = tuple(l1)

# print(l1)
# print(t1)


"""
Question:
Write a program that accepts a comma separated sequence of words as input and prints 
the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""
# userin = input("Enter the comma seperated sequence: ").split(",")
# print(",".join(sorted(userin)))


"""
Question:
Write a program that accepts a sequence of whitespace separated words as input 
and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""
# userin = input("Enter the input sentence: ").split(" ")
# print(" ".join(sorted(list(set(userin)))))


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
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""
# usrin = input("Enter the value of a: ")
# print(int(usrin) + int(2*usrin) + int(3*usrin) + int(4*usrin))

























