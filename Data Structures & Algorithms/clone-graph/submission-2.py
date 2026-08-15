from collections import deque

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

        pairs = dict()

        queue = deque()
        queue.append(node)
        pairs[node] = Node(node.val)

        while queue:

            curr = queue.popleft()

            for n in curr.neighbors:

                if n not in pairs:
                    pairs[n] = Node(n.val)
                    queue.append(n)
                
                pairs[curr].neighbors.append(pairs[n])


        return pairs[node]