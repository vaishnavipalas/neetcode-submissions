class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = dict()

        for n in nums:

            freqs[n] = freqs.get(n, 0)
            freqs[n] += 1

        max_heap = []
        heapq.heapify(max_heap)

        for num, f in freqs.items():
            heapq.heappush(max_heap, [-f, num])

        res = []

        while k and max_heap:
            _, curr = heapq.heappop(max_heap)
            res.append(curr)

            k -= 1

        return res
        