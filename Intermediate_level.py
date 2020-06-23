# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:30:36 2020

@author: aditipc

Description: Intermediate level questions based on Python.
"""

"""
Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
# import math

# def squareroot(array):
#     l1 = array.split(",")
#     C = 50
#     H = 30
#     temp = []
#     for i in range(len(l1)):
#         temp.append(str(round(math.sqrt((2*C*int(l1[i]))/H))))
#     str1 = ",".join(temp)
#     return str1

# user_input = input("Enter a comma seperated sequence: ")
# output = squareroot(user_input)

# print(output)


"""
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""
'''Solution: 1'''
# def twoDarray(row,column):
#     output = []
#     for i in range(int(row)):
#         temp = []
#         for j in range(int(column)):
#             temp.append(i*j)
#         output.append(temp)
#     print(output)

# X,Y = input("Enter the value of row and column: ").split(",")
# twoDarray(X,Y)

'''Solution: 2'''
# X,Y = input("Enter the value of row and column: ").split(",")
# print([[i*j for i in range(int(Y))] for j in range(int(X))])


"""
Question:
Write a program that accepts sequence of lines as input and prints the lines 
after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""
# lines = []
# print("write multiple lines seperated by Enter Key: ")
# while True:
#     line = input()
#     if line:
#         lines.append(line.upper())
#     else:
#         break
# print("\n".join(lines))


"""
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
# temp = []
# for i in range(1000, 3001):
#     num = str(i)
#     if (int(num[0])%2==0) and (int(num[1])%2==0) and (int(num[2])%2==0) and (int(num[3])%2==0):
#         temp.append(num)

# print(",".join(temp))


"""
Question:
Write a program that accepts a sentence and calculate the number of upper case 
letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""
# usrin = input("Enter the input sentence: ")
# u = 0
# l = 0
# for item in usrin:
#     if item.isupper():
#         u += 1
#     elif item.islower():
#         l += 1
# print("UPPER CASE ",u)
# print("LOWER CASE ",l)


"""
Question:
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
"""
# usrin = input("Enter the comma seperated numbers: ").split(",")
# temp = [str(int(item)**2) for item in usrin if int(item)%2 != 0]
# print(",".join(temp))


"""
Question:
Write a program that computes the net amount of a bank account based a transaction 
log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""
# total = 0 
# print("Enter the transaction details: ")
# while True:
#     line = input()
#     if line:
#         l1 = line.split()
#         if l1[0] == 'D':
#             total += int(l1[1])
#         else:
#             total -= int(l1[1])
#     else:
#         break

# print("Account Balance = ", total)


"""
Question:
Please write a program which accepts a string from console and print the characters 
that have even indexes.

Example:
If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:

Helloworld
"""
# userin = input("Enter the input sentence: ")

# '''Method 1'''
# for i in range(len(userin)):
#     if i%2 == 0:
#         print(userin[i], end = "")

# '''Method 2'''
# userin = userin[::2]
# print(userin)


"""
Question:
Please write a program which accepts a string from console and print it in reverse order.

Example:
If the following string is given as input to the program:
rise to vote sir
Then, the output of the program should be:

ris etov ot esir
"""
# userin = input("Enter the input sequence: ")
# print(userin[::-1])


"""
Question:
By using list comprehension, please write a program to print the list after 
removing the value 24 in [12,24,35,24,88,120,155].
"""
# l1 = [12,24,35,24,88,120,155]
# l2 = [x for x in l1 if x != 24]
# print(l2)


"""
Please write a program to print the list after removing delete even numbers 
in [5,6,77,45,22,12,24].
"""
# l1 = [5,6,77,45,22,12,24]
# print([x for x in l1 if x%2 != 0])









