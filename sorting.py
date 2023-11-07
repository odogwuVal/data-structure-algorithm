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
# insertion sort should only be used when your input is small and the data is mostly sorted
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

# insertionSort(unsorted_list)

# Merge Sort
# it is fast and O(nlogn)
# if you are worried about worst case scenario, use merge sort
#  works well when you are not bothered about space complexity
def mergeSort(arr):
    if len(arr) > 1:
        right_arr = arr[len(arr)//2:]
        left_arr = arr[:len(arr)//2]
        mergeSort(left_arr)
        mergeSort(right_arr)

        # merge
        i = 0 #left arr index
        j = 0 #right arr index
        k = 0 #merged arr index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                if right_arr[j] < left_arr[i]:
                    arr[k] = right_arr[j]
                    j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        
# mergeSort(unsorted_list)
# print(unsorted_list)
 

#  Quick sort
def partition(arr, left, right):
    i = left
    j = right-1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j],  arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos-1)
        quicksort(arr, partition_pos+1, right)

quicksort(unsorted_list, 0, len(unsorted_list)-1)
print(unsorted_list)