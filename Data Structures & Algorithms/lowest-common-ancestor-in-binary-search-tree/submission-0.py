class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None: return root
        if root.val == p.val: return p
        if root.val == q.val: return q
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l != None and r != None:
            return root
        if l != None:
            return l
        if r != None:
            return r
        return None