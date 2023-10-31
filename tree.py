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
    
    def remove(self, data):
        if not self.root:
            return False
        
        current_node = self.root
        parent = None
        while current_node:
            if data < current_node.data:
                parent = current_node
                current_node = current_node.left
            elif data > current_node.data:
                parent = current_node
                current_node = current_node.right
            elif data == current_node.data:
                # No right child
                if not current_node.right:
                    if parent == None:
                        self.root = current_node.left
                    else:
                        # if parent > current data, current left child becomes a child of parent
                        if current_node.data < parent.data:
                            parent.left = current_node.left
                        # if parent < current data, current left child becomes a right child of parent
                        if current_node.data > parent.data:
                            parent.right = current_node.left
                # Right child which does not have a left child
                elif current_node.right.left == None:
                    current_node.right.left = current_node.left
                    if parent == None:
                        self.root = current_node.right
                    else:
                        #//if parent > current, make right child of the left the parent
                      if current_node.data < parent.data:
                          parent.left = current_node.right
                      #//if parent < current, make right child a right child of the parent
                      elif current_node.data > parent.data:
                          parent.right = current_node.right


                #Option 3: Right child that has a left child
                else:
                    #find the Right child's left most child
                    leftmost = current_node.right.left
                    leftmostParent = current_node.right
                    while leftmost.left != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    #Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right

                    if parent == None:
                        self.root = leftmost
                    else:
                        if current_node.data < parent.data:
                            parent.left = leftmost
                        elif current_node.data > parent.data:
                            parent.right = leftmost
        return True


mytree = BinarySearchTree()
mytree.insert(6)
mytree.insert(7)
mytree.insert(3)
mytree.insert(8)
print(mytree.lookup(3))
mytree.print_tree()