# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        indexing = {}

        pre_index = 0

        for i in range(0, len(inorder)):
            indexing[inorder[i]] = i

        def build(preorder, inorder, left, right):
            nonlocal pre_index
            if right < left:
                return None
            element = preorder[pre_index]
            pre_index += 1
            index = indexing[element]
            current_node = TreeNode(element)
            current_node.left = build(preorder, inorder, left, index - 1)
            current_node.right = build(preorder, inorder, index + 1, right)
            return current_node

        return build(preorder, inorder, 0, len(inorder) - 1)
