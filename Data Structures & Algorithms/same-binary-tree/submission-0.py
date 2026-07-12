# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p == None and q == None): return True
        if (p == None and q != None): return False
        if (p != None and q == None): return False
        lVal = self.isSameTree(p.left, q.left)
        rVal = self.isSameTree(p.right, q.right)
        if lVal and rVal and p.val == q.val: return True
        return False

        