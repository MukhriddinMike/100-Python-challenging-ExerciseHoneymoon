'''
Write a program which accepts a sequence of comma-separated numbers from
console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')


'''

value = input() # input nums with comma so it will be one string
list = value.split(',') # divede into parts where it has ','
l = [i.strip(' ') for i in list] # you can skip but better to remove extra spaces
tuple = tuple(l) # cast to tuple

print(l)
print(tuple)

