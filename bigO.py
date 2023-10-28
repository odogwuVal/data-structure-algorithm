import time

nemo = ['nemo' for i in range(10)]
medium_nemo = ['nemo' for i in range(100)]
big_nemo = ['nemo' for i in range(100000)]

def find_nemo(array):
    t0 = time.time()
    print(array)
    t1 = time.time()
    print(f'it took {t1 - t0} milliseconds to find nemo')
# find_nemo(big_nemo)

# O(n) => Linear Time
# O(1) => Constant Time
# O(n^2) => Quadratic time
boxes = [1, 2, 3, 4, 5, 6]

def log_array_pairs(array):
    for i in boxes:
        for j in boxes:
            print(i, j)

# log_array_pairs(boxes)

# Drop Non Dominants(example)
def printAllNumbersThenAllPairSums(numbers):
    print('These are the numbers:')
    for i in numbers: # O(n)
        print(i)
    print('and these are there sums')
    for i in numbers: #O(n^2)
        for j in numbers:
            print(i + j)
# printAllNumbersThenAllPairSums([1, 2, 3, 4, 5, 6])
# BIG O => O(n + n^2) => O(n^2) since O(n) is not dominant

# RULE BOOK FOR BIG O
# Worst Case
# Remove Constants
# Different terms for inputs
# Drop Non Dominants

# SPACE COMPLEXITY
# A program remembers things during execution using the heap or the stack
# Heap is usually where variables are stored
# Stack is how the function calls are tracked
# 

# # Space complexity is cause by:
# variables
# Function calls
# Data structure
# Allocations



def booo(n):
    for i in n:
        print('booo')
# Space complexity only cares about the additional space and not the space taken up by the input
# The space complexity here is O(1) because we are only storing variables to i

def TestSpace(n):
    hiArray = [] # O(n)
    for i in n: # O(1)
        hiArray[i] = 'hi'
    return hiArray
# space complexity here is O(n)

# Given 2 arrays/lists, create a function that lets a user know whether 
# these two arrays contain any common items
# Example
# arr_one = ['a', 'b', 'c', 'x']
# arr_two = ['z', 'y', 'i']
# should return false

# arr_one = ['a', 'b', 'c', 'x']
# arr_two = ['z', 'y', 'x']
# should return true

# brute force
def commonItems(array_one, array_two):
    for i in array_one:
        for j in array_two:
            if i == j:
                return True
    return False
# print(commonItems(arr_one, arr_two))

# using a hash table
def commonItemsHash(array_one, array_two):
    hash_table = dict()
    for i in range(len(array_one)):
        hash_table[array_one[i]] = True

    for i in range(len(array_two)):
        if array_two[i] in hash_table:
            return True
    return False