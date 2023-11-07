# Binary Search

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

    # bFS
    def breadthFirstSearch(self):
        current_node = self.root
        # to store the visited nodes
        my_list = []
        # to queue the nodes to be visited
        my_queue = []
        my_queue.append(current_node)

        while len(my_queue) > 0:
            current_node = my_queue[0]
            del my_queue[0]
            my_list.append(current_node.data)
            if current_node.left:
                my_queue.append(current_node.left)
            if current_node.right:
                my_queue.append(current_node.right)
        return my_list

    def breadthFirstSearchRecursive(self, myqueue, mylist):
        if len(myqueue) == 0:
            return mylist
        current_node = myqueue[0]
        del myqueue[0]
        mylist.append(current_node.data)

        if current_node.left:
            myqueue.append(current_node.left)
        if current_node.right:
            myqueue.append(current_node.right)
        
        return self.breadthFirstSearchRecursive(myqueue, mylist)

        # DFS

        #     9
        # 4           20
    # 1       6   15      170

    # Inorder = [1, 4, 6, 9, 15, 20, 170]
    # preorder = [9, 4, 1, 6, 20, 15, 170]
    # postorder = [1, 6, 4, 15, 170, 20, 9]
    def inOrder(self, current_node, mylist):
        if current_node:
            self.inOrder(current_node.left, mylist)
            mylist.append(current_node.data)
            self.inOrder(current_node.right, mylist)
        return mylist

    def preOrder(self, current_node, mylist):
        if current_node:
            mylist.append(current_node.data)
            self.preOrder(current_node.left, mylist)
            self.preOrder(current_node.right, mylist)
        return mylist

    def postOrder(self, current_node, mylist):
        if current_node:
            self.postOrder(current_node.left, mylist)
            self.postOrder(current_node.right, mylist)
            mylist.append(current_node.data)
        return mylist

mytree = BinarySearchTree()
mytree.insert(6)
mytree.insert(7)
mytree.insert(3)
mytree.insert(8)
print(mytree.lookup(3))
mytree.print_tree()
print(mytree.breadthFirstSearch())
print(mytree.breadthFirstSearchRecursive([mytree.root], []))
print(mytree.inOrder(mytree.root, []))
print(mytree.preOrder(mytree.root, []))
print(mytree.postOrder(mytree.root, []))
    
     


# Depth first search {has a lower memory requirement}