from collections import deque
import time
import threading

class Stack:
    def __init__(self):
        self.arr = []
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        if self.length < 1:
            print(f'No item in list')
            return
        print(self.arr[self.length-1])
        return

    def push(self, value):
        self.arr.append(value)
        self.length += 1

    def pop(self):
        popped_item = self.arr[self.length-1]
        del self.arr[self.length-1]
        self.length -= 1
        return popped_item

# mystack = ArrayStack()
# mystack.push(8)
# mystack.push(4)
# mystack.push(15)
# mystack.pop()
# mystack.peek()
# print(mystack)

# Queues
class Queues:
    def __init__(self):
        self.buffer = deque()
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.buffer[self.length-1]
    
    def enqueue(self, data):
        self.buffer.appendleft(data)
        self.length += 1

    def dequeue(self):
        if self.length < 1:
            print('queue is empty')
            return
        popped_item = self.buffer.pop() 
        self.length -= 1
        return popped_item

myqueue = Queues()
myqueue.enqueue(8)
myqueue.enqueue(4)
myqueue.enqueue(2)
myqueue.enqueue(12)
myqueue.enqueue(34)
print(myqueue.peek()) 
myqueue.dequeue()
print(myqueue)