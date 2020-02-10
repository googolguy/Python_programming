# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:27:35 2020

@author: aditipc

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
def numbers():
    temp = []
    for i in range(2000,3201):
        if ((i%7 == 0) and (i%5 != 0)):
            temp.append(str(i))
    return temp

out = numbers()
print(",".join(out))
