# A hash function is a function that generates a fixed length for each input it gets
# example: md5, SHA-1, SHA-256(takes a longer time) etc
# Hash functions are one way...in that you cannot get back the input from a hash
# The hash output will always return the same
# A slight diffrenece in input will return a completely different hash
class Hashtable:
    def __init__(self):
        """
        Create an array(self.mydict) with a bucket size - which is derived from the load factor.
        The load factor is a measure that decides when to increase the hashmap capacity to maintain the get() and put()
        operation complexity of O(1).
        the default load factor of HashMap is 0.75f(75% of the map size).
        Load factor = (n/k)
        where n is the max number of elements that can be stored in dict
        k is the bucket size
        Optimal Load factor is around (2/3) such that the effect of hash collision is minimal 
        """
        self.bucket = 16
        self.hashmap = [[] for i in range(self.bucket)]

    def __str__(self):
        return str(self.__dict__)

    def hash(self, key):
        return len(key) % self.bucket
    
    def althash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.bucket


    def put(self, key, value):
        """
        Value may already be present
        """
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference[i][1] = value
                return None
        reference.append([key, value])
        return None

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                return reference[i][1]
        return -1
    
    def remove(self, key):
        """
        Removes the value of a specified value key if this map contains a mapping for the key
        """
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference.pop(i)
                return None
        return None

class HashMapTwo:
    def __init__(self):
        self.bucket = 20
        self.map = [[] for i in range(self.bucket)]

    def __str__(self):
        return str(self.__dict__)
    
    def hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.bucket

    def __setitem__(self, key, value):
        hash_value = self.hash(key)
        reference = self.map[hash_value]
        for idx, element in enumerate(reference):
            if element[0] == key:
                reference[idx] = (key, value)
                return None
        reference.append((key, value))
        return None
    
    def __getitem__(self, key):
        hash_value = self.hash(key)
        reference = self.map[hash_value]
        for idx, element in enumerate(reference):
            if element[0] == key:
                print(element[1])
        return -1
    
    def __delitem__(self, key):
        hash_value = self.hash(key)
        reference = self.map[hash_value]
        for idx, element in enumerate(reference):
            if element[0] == key:
                del reference[idx]
        return None

    def getKeys(self):
        keys = []
        if self.map:
            for i in self.map:
                if len(i) >= 1:
                    for j in i:
                        keys.append(j[0])
        return keys



# t = HashMapTwo()
# print(t.hash('circle'))
# t['grapes'] = 100
# t['apples'] = 10
# t['ora'] = 300
# t['grapes'] = 75
# print(t)
# t['ora']
# # del t['apples']
# print(t)
# print(t.getKeys())

# h = Hashtable()
# h.put('grapes',1000)
# h.put('apples',10)
# h.put('apples',68)
# h.put('ora',300)
# print(h)-

# Given an array [2, 5, 1, 2, 3, 5, 1, 2, 4]
# return the first recurring character...this should return 2
# return -1 if there is no recuring character

def recurringCharacter(char):
    mydict = dict()
    for item in range(len(char)):
        if char[item] in mydict.values():
            return char[item]
        mydict[item] = char[item]
    return None

mylist = [2, 5, 5, 1, 2, 3, 5, 1, 2, 4]
# mylist = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# mylist = [2, 3, 4, 5]
# mylist = [4, 1, 2, 3, 5, 4]
print(recurringCharacter(mylist))