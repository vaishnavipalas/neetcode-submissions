"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        seen = dict()

        def dfs(node):

            if not node:
                return None

            if node.val in seen:
                return seen[node.val]
                
            curr = Node(node.val)
            seen[node.val] = curr

            for n in node.neighbors:
                curr.neighbors.append(dfs(n))

            return curr

        return dfs(node)

            



            



        