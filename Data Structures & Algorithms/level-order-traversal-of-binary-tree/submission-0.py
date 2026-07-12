# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        from collections import deque
        q = deque()
        q.append(root)
        finList = []

        while len(q) > 0:
            arrList = []
            qLen = len(q)
            for _ in range(qLen):
                element = q.popleft()
                arrList.append(element.val)
                if element.left: q.append(element.left)
                if element.right: q.append(element.right)
            if len(arrList) > 0:
                finList.append(arrList)

        print(finList)
        return finList


        