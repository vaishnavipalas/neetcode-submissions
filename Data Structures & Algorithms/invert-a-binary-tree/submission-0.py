# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(T):
            if not T:
                return

            left = T.left
            right = T.right

            T.left = invert(right)
            T.right = invert(left)

            return T

        return invert(root)
        
        