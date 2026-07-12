class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        def height(node):
            if not node:
                return 0
            l = height(node.left)
            r = height(node.right)
            self.best = max(self.best, l + r)
            return max(l, r) + 1
        height(root)
        return self.best