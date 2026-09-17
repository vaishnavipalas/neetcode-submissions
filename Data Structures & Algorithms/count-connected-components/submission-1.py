class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # plan: as we process the edges, if the two nodes aren't already connected
        #       then we connect them. that means the number of total components goes down

        # we know that two nodes are connected if they have the same parent node
        numComponents = n


        unionFind = [i for i in range(n)]

        def find(x):

            if unionFind[x] != x:
                return find(unionFind[x])
            return x

        def union(x, y):

            unionFind[find(y)] = find(x)

        cache = dict()


        for n1, n2 in edges:

            parent1 = find(n1)
            parent2 = find(n2)

            if parent1 != parent2:
                union(n1, n2)
                numComponents -= 1

        return numComponents



            


        
