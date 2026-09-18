class MedianFinder:

    def __init__(self):

        self.lo = []
        heapq.heapify(self.lo)

        self.hi = []
        heapq.heapify(self.hi)
        

    def addNum(self, num: int) -> None:

        heapq.heappush(self.lo, -num)

        if self.lo and self.hi and (-self.lo[0] > self.hi[0]):
            heapq.heappush(self.hi, -heapq.heappop(self.lo))

        if len(self.lo) - len(self.hi) > 1:
            heapq.heappush(self.hi, -1*heapq.heappop(self.lo))
        elif len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -1 * heapq.heappop(self.hi))
        

    def findMedian(self) -> float:

        if len(self.lo) > len(self.hi):
            return float(self.lo[0] * -1)

        return (-self.lo[0] + self.hi[0]) / 2.0





        
        