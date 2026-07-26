import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        max_heap = []

        for s in stones:
            heapq.heappush(max_heap, -s)

        while len(max_heap) > 1:
            y = -1 * heapq.heappop(max_heap)
            x = -1 * heapq.heappop(max_heap)

            if x == y:
                continue
            elif x < y:
                y = y - x
                heapq.heappush(max_heap, -y)

        return -1 * max_heap[0] if max_heap else 0
        