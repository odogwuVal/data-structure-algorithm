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
