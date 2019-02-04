'''
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

'''
"""
#####################
#version 1

import  math
H = 30
C = 50
m= list()
def squad(D):
    for item in D:
        Q =math.sqrt((2 * C * int(item))/H)
        print(round(Q),end=",")


value = input()
list = value.split(",")
D =[i.strip(" ") for i in list]
squad(D)

"""
import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print (','.join(value))
