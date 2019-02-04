'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

'''
# version 1
'''
class two_numbers:

    def __init__(self,f_num,s_num):
        self.firstNumber = f_num
        self.secondNumber = s_num

    def show(self):
        print(self.firstNumber)
        print(self.secondNumber)

N1 = int(input())
N2 = int(input())
c1 = two_numbers(N1, N2)
c1.show()

'''

# version 2

class inputString():
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


str = inputString()

str.getString()

str.printString()