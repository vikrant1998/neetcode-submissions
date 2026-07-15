class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        # a valid BST's in-order walk is strictly increasing
        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False
        return True