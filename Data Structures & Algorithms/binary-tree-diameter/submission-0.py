# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        d = 0

        def depth(T):

            nonlocal d

            if not T:
                return 0

            l = depth(T.left)
            r = depth(T.right)

            d = max(d, l + r)

            return 1 + max(l, r)

        if not root:
            return 0

        depth(root)

        return d
        