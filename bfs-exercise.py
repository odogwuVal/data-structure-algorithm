class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.right = None
        self.left = None
    
class BinaryTree():
    def __init__(self):
        self.root = None

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