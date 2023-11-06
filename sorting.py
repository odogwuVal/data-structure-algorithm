# Bubble sort
# this is the least efficient
def bubbleSort(arr):
    a = 0
    # this will make sure that we sort the entire length of the array
    while a < len(arr):
        # this checks for the two elements side by side and swaps when needed
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i] # replacement in python
        a += 1
    return arr

unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
# print(bubbleSort(unsorted_list))

# selection sort
def selectionSort(arr):
    a = 0
    while a < len(arr):
        smallest_number = arr[a]
        index = a
        for j in range(a+1, len(arr)):
            if arr[j] < smallest_number:
                index = j
                smallest_number = arr[j]
        arr[a], arr[index] = arr[index], arr[a]
        a += 1
    return arr

# print(selectionSort(unsorted_list))

# Insertion sort
def insertionSort(arr):
    length = len(arr)
    i = 1
    end = arr[0]
    while i < length:
        if arr[i] < end:
            x = arr.pop(i)
            for j in range(0, i):
                if x < arr[j]:
                    arr.insert(j, x)
                    break
        end = arr[i]
        i += 1
    return arr

insertionSort(arr)