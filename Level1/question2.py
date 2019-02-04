'''
/Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
/
/
'''
N = 8
m = 1
for i in range(1,N+1):
    m=m*i
print(m)
# I will be back and will make it easier
# map,list comp, lambda etc.
# or

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))
