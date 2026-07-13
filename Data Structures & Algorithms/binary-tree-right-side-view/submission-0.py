# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        from collections import deque
        q = deque()
        q.append(root)
        res = []

        while len(q) > 0:
            qLen = len(q)
            while qLen > 0:
                element = q.popleft()
                if element.left: q.append(element.left)
                if element.right: q.append(element.right)
                if qLen == 1: res.append(element.val)
                qLen -= 1

        return res


        