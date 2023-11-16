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

class Solution(object):
    def isValidBSTEfficient(self, root):
        def bfs_helper(node, parent_max, parent_min):
            if not node:
                return True

            elif node.data >= parent_max and node.data <= parent_min:
                return False

            else:
                return bfs_helper(node.left, node.data, parent_min) and bfs_helper(node.right, parent_max, node.data)
        return bfs_helper(root, float('inf'), float('-inf'))
    # you are given the root of a binary search tree(BST), where the values of exactly two nodes of the tree were swapped by mistake
    # Recover the tree without changing its structure
    def inorder(self, root, arr):
        if not root:
            return arr
        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)

    def inorder_fix(self, root, v1, v2):
        if not root:
            return
        if root.data == v1:
            root.data = v2
        if root.data == v2:
            root.data = v1
        self.inorder_fix(root.left, v1, v2)
        self.inorder_fix(root.right, v1, v2)

    def recoverTree(self, root):
        arr = []
        self.inorder(root, arr)
        sorted_arr = sorted(arr)

        v1 = None
        v2 = None

        for i in range(0, len(arr)):
            if arr[i] != sorted_arr[i]:
                if v1 == None:
                    v1 = arr[i]
                else:
                    v2 = arr[i]
        self.inorder_fix(root, v1, v2)

    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.data == right.data:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        return False

    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    




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
# print(mytree.isValidBSTEfficient(float('inf'), float('-inf')))

mysolution = Solution()
print(mysolution.isValidBSTEfficient(mytree))
mysolution.recoverTree(mytree)
print(mysolution.isSymmetric(mytree))
        # 7
    # 5           #9
 #4      #6    #8     #10