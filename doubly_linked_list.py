class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def print(self):
        mylinkedlist = ''
        current_node = self.head
        while current_node:
            mylinkedlist += str(current_node.data) + '<==>'
            current_node = current_node.next
        print(f'<=={mylinkedlist}')
    
    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
            return
        new_node = Node(data)
        tmp = self.head
        self.head.prev = new_node
        new_node.next = tmp
        self.head = new_node
        return
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data)


dlist = DoublyLinkedList()
dlist.append(45)
dlist.append(36)
dlist.append(17)
dlist.prepend(7)
dlist.prepend(8)
dlist.prepend(72)
dlist.insert(4, 26)
dlist.remove(6)
dlist.print()