class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # inputs: n - there are n nodes labeled 0 to n -1
        #         list of edges that are undirected [node1, node3]
        # output: bool true if there are no cycles and the entire graph is connected


        # keep track of the parents of the nodes are you visit them
        # perform a bfs or dfs starting from 0 and for its children, if the 
        #   node was already visited, check its parent. if that parent is not
        #   the node we are at right now, then there is a cycle


        # if we were able to go visit all the nodes, return true but only if the length
        #   of visited is n. otherwise, that means there was a segment that was not 
        #   connected

        if len(edges) != n -1:
            return False
        
        graph = {}

        for n1, n2 in edges:
            graph[n1] = graph.get(n1, []) + [n2]
            graph[n2] = graph.get(n2, []) + [n1]


        queue = deque()

        queue.append([-1, 0]) # (parent, node)

        visited = set()
        visited.add(0)

        while queue:

            parent, curr = queue.popleft()

            for child in graph.get(curr, []):

                if child in visited:
                    if child != parent:
                        return False
                    else:
                        continue

                queue.append((curr, child))
                visited.add(child)

        return len(visited) == n




        