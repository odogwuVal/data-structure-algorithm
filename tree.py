#  Binary tree
# each node can only have eith zero, one or two nodes
# each child can only have one parent
# A node either has zero or two children but never one child 

#  Binary search trees
# All child nodes to the right of the root node must be greater than the parent node
# All child nodes to the left of the root node must be less than the parent node
class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def print(self, current_node):
        if current_node:
            self.print(current_node.left)
            print(str(current_node.data))
            self.print(current_node.right)
        
    def print_tree(self):
        if self.root:
            self.print(self.root)

    def insert(self, data):
        if not self.root:
            self.root = BinaryNode(data)
            return
        current_node = self.root
        while True:
            # left
            if data < current_node.data:
                if not current_node.left:
                    current_node.left = BinaryNode(data)
                    return
                else:
                    current_node = current_node.left
            # right
            elif data > current_node.data:
                if not current_node.right:
                    current_node.right = BinaryNode(data)
                    return
                else:
                    current_node = current_node.right
            
    def lookup(self, data):
        current_node = self.root
        while True:
            if not current_node:
                return False
            if current_node.data == data:
                return True
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

mytree = BinarySearchTree()
mytree.insert(6)
mytree.insert(7)
mytree.insert(3)
mytree.insert(8)
print(mytree.lookup(3))
mytree.print_tree()