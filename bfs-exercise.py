class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.right = None
        self.left = None

    def insert(self, data):
        if data == self.data:
            return

        # insert in the left
        if data < self.data:
            if not self.left:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        
        # insert in the right
        else:
            if not self.right:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

    def inorder_traversal(self):
        element = []
        if self.left:
            element += self.left.inorder_traversal()
        element.append(self.data)
        if self.right:
            element += self.right.inorder_traversal()
        return element

    def isSameTree(self, p, q):
        # p and q are Tree Nodes

        # return false if either p or q is None
        if p is None or q is None:
            return False
        
        # return true if p and q are both None
        if p is None and q is None:
            return True

        # check if the data in both nodes are the same, return False if they aren't
        if p.data == q.data:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

    def bfs(self):
        if not self.data:
            return
        
        queue = []
        bfs_output = ''
        queue.append(self)

        while len(queue) != 0:
            self = queue.pop(0)
            bfs_output += str(self.data) + '==>'

            if self.left:
                queue.append(self.left)
            if self.right:
                queue.append(self.right)
        return bfs_output

    def height(self):
        if self.left and self.right:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left:
            return 1 + self.left.height()
        elif self.right:
            return 1 + self.right.height()
        else:
            return 1

    def isValidBST(self):
        if self:
            if self.left:
                if self.left.data > self.data:
                    return False
                else:
                    self.left.isValidBST()
            if self.right:
                if self.right.data < self.data:
                    return False
                else:
                    self.right.isValidBST()
        return True 

    def isValidBSTEfficient(self, parent_max, parent_min):
        pass      




mytree = TreeNode(7)
mytree.insert(5)
mytree.insert(9)
mytree.insert(4)
mytree.insert(6)
mytree.insert(8)
mytree.insert(10)
print(mytree.height())
print(mytree.inorder_traversal())
print(mytree.bfs())
# print(mytree.isValidBST())
print(mytree.isValidBSTEfficient(float('inf'), float('-inf')))
        # 7
    # 5           #9
 #4      #6    #8     #10