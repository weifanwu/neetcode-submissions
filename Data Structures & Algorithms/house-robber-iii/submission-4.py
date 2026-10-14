# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def search(self, node: TreeNode, choose: int, memo: List) -> int:
        if not node:
            return 0
        if (node, choose) in memo:
            return memo[(node, choose)]

        currentTotal = node.val if choose == 0 else 0

        if choose == 1:
            currentTotal += max(self.search(node.left, 0, memo), self.search(node.left, 1, memo))
            currentTotal += max(self.search(node.right, 0, memo), self.search(node.right, 1, memo))
        else:
            currentTotal += self.search(node.left, 1, memo)
            currentTotal += self.search(node.right, 1, memo)
        
        memo[(node, choose)] = currentTotal
        return currentTotal
            

    def rob(self, root: Optional[TreeNode]) -> int:

        memo = {}

        return max(self.search(root, 0, memo), self.search(root, 1, memo))