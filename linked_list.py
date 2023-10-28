class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data)
        
    def print(self):
        mylinkedlist = ''
        current_node = self.head
        while current_node:
            mylinkedlist += str(current_node.data) + '==>'
            current_node = current_node.next
        print(mylinkedlist)
    
    def prepend(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
    
    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return
        length = 0
        current_node = self.head
        while current_node:
            if length+1 == index:
                tmp = current_node.next
                current_node.next = Node(data)
                current_node.next.next = tmp
                return
            current_node = current_node.next
            length += 1
        print(f'{index} is out of range')

    def remove(self, index):
        if index == 0:
            tmp = self.head.next
            self.head.next = None
            self.head = tmp
            return
        length = 0
        current_node = self.head
        while current_node:
            if length+1 == index:
                tmp = current_node.next.next
                current_node.next.next = None
                current_node.next = tmp
                return
            current_node = current_node.next
            length += 1
        print(f'{index} is out of range')

    def reverse(self):
        if not self.head:
            return

        prev = None
        current_node = self.head
        while current_node:
            tmp = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = tmp
        self.head = prev

mylist = LinkedList() 
mylist.append(5)
mylist.append(8)
mylist.append(15)
mylist.prepend(2)
mylist.prepend(30)
mylist.insert(2, 45)
mylist.insert(0, 15)
mylist.insert(7, 36)
# mylist.insert(10, 37)
mylist.reverse()
# mylist.remove(3)
mylist.print()