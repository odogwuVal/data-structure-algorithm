# Understanding recursion
# A recurssive function needs an allocation from the memory to remember the past calls.
# this memory location is called a stack...the functions are stacked there till a base case is hit, 
# and the content of the stack gets returned
# In the absence of a base case, you get a stack overflow
counter = 0
def inception():
    global counter
    if counter > 6:
        return 'done'
    else:
        counter += 1
        return inception()
        

# inception()

# Write a function that finds the factorial of any number.
# Write the function recurssively and iteratively
def factorialRecursion(n):
    if n == 1:
        return 1
    else:
        return n * factorialRecursion(n-1)

# factorialRecursion(3)

def factorialIterative(n):
    counter = 1
    result = 1
    while counter <= n:
        result = result * counter
        counter += 1
    return result 

# factorialIterative(5)

# Fibonacci sequence
# Given a number, return the index value of the fibonacci sequence, where the sequence is:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
# the pattern of the sequence is that each value is the sum of the two previous values, that means 
# that for N=5 -> 2+3

def fib_iterative(n):
    if n < 2:
        return n
    a = 0
    b = 1
    total = 0
    for i in range(n-1):
        total = a + b
        a = b
        b = total
    return total

def fib_recurssive(n):
    if n < 2:
        return n
    return fib_recurssive(n-1) + fib_recurssive(n-2)


# print([fib_recurssive(i) for i in range(5)])
# print([fib_iterative(i) for i in range(5)])

def reverseStr(string):
    mystr = []
    for i in range(len(string)-1, -1, -1):
        mystr.append(string[i])
    reversed_str = ''.join(mystr)
    return reversed_str

# print(reverseStr('hello'))

def reverseStrRec(string):
    size = len(string)
    if size == 0:
        return
    last_char = string[size-1]
    print(last_char, end='')
    return reverseStrRec(string[0:size-1])

reverseStrRec('hello')