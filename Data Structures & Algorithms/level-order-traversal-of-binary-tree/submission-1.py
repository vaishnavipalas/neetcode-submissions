# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        q = deque()

        if not root:
            return []

        q.append(root)

        res = []

        while q:

            l = len(q)
            level = []

            for _ in range(l):
                curr = q.popleft()
                level.append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            res.append(level)

        return res





        