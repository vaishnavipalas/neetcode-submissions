"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        new_graph = dict()

        def dfs(node):

            if not node:
                return None


            curr = Node(node.val)
            new_graph[node.val] = curr

            for n in node.neighbors:
                if n.val in new_graph:
                    curr.neighbors.append(new_graph[n.val])
                else:
                    curr.neighbors.append(dfs(n))

            return curr

        return dfs(node)

            



            



        