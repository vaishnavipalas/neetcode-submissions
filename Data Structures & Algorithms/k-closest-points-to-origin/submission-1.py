import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def find_dist(x2, y2):

            under_root = (x2 - 0) ** 2 + (y2 - 0) ** 2
            return under_root ** 0.5

        min_heap = []


        for x, y in points:
             dist = find_dist(x ,y)

             heapq.heappush(min_heap, (dist, [x, y]))
        
        print(min_heap)

        ans = []

        while k > 0:
            _, P = heapq.heappop(min_heap)
            ans.append(P)
            k -= 1

        return ans




        