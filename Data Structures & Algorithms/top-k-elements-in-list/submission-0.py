import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get freqs of all the elems
        freqs = Counter(nums)

        # make a priority queue
        pq = []

        for key in freqs:
            heapq.heappush(pq, (-freqs[key], key))
        
        # get result by popping top k elements
        result = []
        for _ in range(k):
            _, num = heapq.heappop(pq)
            result.append(num)

        return result
