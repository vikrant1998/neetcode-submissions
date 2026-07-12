# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.yes = False

    def isTree(self, t1, t2):
        if t1 == None and t2 == None: return True
        if t1 == None and t2 != None: return False
        if t1 != None and t2 == None: return False
        if t1.val != t2.val: return False
        lVal = self.isTree(t1.left,  t2.left)
        rVal = self.isTree(t1.right, t2.right)
        return lVal and rVal

    def subCheck(self, root, subRoot):
        if root == None: return

        self.subCheck(root.left, subRoot)
        self.subCheck(root.right, subRoot)

        if self.isTree(root, subRoot):
            self.yes = True


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.subCheck(root, subRoot)
        return self.yes
        