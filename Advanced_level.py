# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:31:08 2020

@author: aditipc
"""

"""
Question:
Write a program to solve a classic ancient Chinese puzzle.
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have?
"""
# def puzzle(h,l):
#     h = int(h)
#     l = int(l)
#     for i in range(h+1):
#         j = h - i
#         if (4*i)+(2*j) == l:
#             print("Rabbits: ",i, end = " ")
#             print("Chickens: ",j, end = "\n")
#             return
#     print("No possible solution")
#     return

# heads,legs = input("Enter total number of heads and legs: ").split()
# solution = puzzle(heads,legs)


"""
Question:
Please write a program which count and print the numbers of each character in 
a string input by console.

Example:
If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1
"""
# userin = [str(x) for x in input("Enter the input sequence: ")]
# unique = set(userin)
# l1 = list(unique)
# dict1 = {}

# for item in l1:
#     dict1[item] = userin.count(item)

# for k,v in sorted(dict1.items()):
#     print(k,v)


"""
Question:
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print 
this list after removing all duplicate values with original order reserved.
"""
# def remove_duplicates(l1):
#     l2 = list(set(l1))
#     temp = []
#     for item in l1:
#         if item in l2:
#             temp.append(item)
#             l2.remove(item)
#     return temp

# l1 = [12,24,35,24,88,120,155,88,120,155]
# unique = remove_duplicates(l1)
# print(unique)


"""
Question:
By using list comprehension, please write a program to print the list after 
removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
"""
# l1 = [12,24,35,70,88,120,155]
# l2 = [x for x in l1 if l1.index(x) not in [0,4,5]]
# print(l2)


"""
Question:
By using list comprehension, please write a program generate a 3*5*8 3D array 
whose each element is 0.
"""
# array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
# print(array)


"""
Question:
By using list comprehension, please write a program to print the list after 
removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
"""
# l1 = [12,24,35,70,88,120,155]
# l2 = [x for x in l1 if l1.index(x)%2 != 0]
# print(l2)


"""
Question:
By using list comprehension, please write a program to print the list after 
removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
"""
# l1 = [12,24,35,70,88,120,155]
# l2 = [x for x in l1 if (x%5 != 0) and (x%7 != 0)]
# print(l2)


"""
Question:
Please write a program to generate all sentences where subject is in ["I", "You"] 
and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
"""
# subject = ["I", "You"]
# verb = ["Play", "Love"]
# objects = ["Hockey","Football"]
# for i in subject:
#     for j in verb:
#         for k in objects:
#             print(i+" "+j+" "+k)









