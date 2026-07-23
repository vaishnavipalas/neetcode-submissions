# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, min, max):

            if not node:
                return True

            if node.left and not (min < node.left.val < node.val):
                return False

            if node.right and not (node.val < node.right.val < max):
                return False

            return helper(node.left, min, node.val) and helper(node.right, node.val, max)

        return helper(root, float('-inf'), float('inf'))

        
        