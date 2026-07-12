# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.yes = True

    def height(self, root):
        if root == None: return 0
        l = self.height(root.left)
        r = self.height(root.right)
        if abs(l - r) > 1: self.yes = False
        return max(l, r) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)
        return self.yes
        