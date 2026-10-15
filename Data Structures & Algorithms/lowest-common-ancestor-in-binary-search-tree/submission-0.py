# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = None

        def search(node, p, q):
            if not node:
                return 0
            current = (1 if (node.val == p.val or node.val == q.val) else 0) + search(node.left, p, q) + search(node.right, p, q)
            if (current == 2) and (not self.res):
                self.res = node
            return current

        search(root, p, q)
        return self.res if self.res else TreeNode()

        