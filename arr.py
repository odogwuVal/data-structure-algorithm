class myArray:
    def __init__(self): 
        self.length=0
        self.data={}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length]=item
        self.length+=1

    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return last_item

    def delete(self, index):
        deleted_item = self.data[index]
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length-=1
        return deleted_item



arr=myArray()
arr.push('hi')
arr.push('how')
arr.push('you')
arr.push('more')
arr.push('yes')
arr.delete(2)
print(arr)

# Create a function that reverses a string:
# Hi my name Madu Valentine should be:
# should be returned in reverse
def reverse_str(stri):
    if not isinstance(stri, str) or len(stri) < 2:
        print("Use valid chat=racters")
    else:
        my_list = []
        for i in range(len(stri)-1, -1, -1):
            my_list.append(stri[i])
        
        return ''.join(my_list) 
name = 'Hi my name Madu Valentine'
# name = 45
# print(reverse_str(name))

def reverse_str2(stri):
    my_list = ''.join([stri[i] for i in range(len(stri)-1,-1,-1)])
    print(my_list)

# reverse_str2(name)

# Write a function to Merge two sorted arrays into one
# [0,3,4,31] [4,6,30]
a = [0,3,4,31]
b = [4,6,30]

# first method
def mergeSortedArray(a, b):
    merged = a + b
    sorted(merged)
    return merged
# print(mergeSortedArray(a,b))

# interview method of solving the same
def mergeSortedArray2(a,b):
    if len(a) == 0 or len(b) == 0:
        return a+b
    my_list = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            my_list.append(a[i])
            i += 1
        elif b[j] <= a[i]:
            my_list.append(b[j])
            j += 1

    return my_list+a[i:]+b[j:]
 
print(mergeSortedArray2(a,b))

# Importance of arrays
# 1. For fast look ups where you know the indexes
# 2. Fast push/pop
# 3. It is ordered too

# Disadvantages
# 1. Slow inserts and deletes because you have to shift the entire array
