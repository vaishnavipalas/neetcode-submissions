# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inord_idx = dict()

        for i in range(len(inorder)):
            inord_idx[inorder[i]] = i

        def helper(pre_idx, l, r):
            if not pre_idx < len(preorder):
                return None

            if l > r:
                return None
            
            root = TreeNode(preorder[pre_idx])

            root_idx = inord_idx[root.val]

            root.left = helper(pre_idx + 1, l, root_idx - 1)
            root.right = helper(pre_idx + root_idx - l + 1,
                            root_idx + 1,
                            r)
            return root

        return helper(0, 0, len(inorder))


        