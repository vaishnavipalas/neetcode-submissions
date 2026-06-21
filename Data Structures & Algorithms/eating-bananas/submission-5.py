import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lo = 1
        hi = max(piles)

        res = hi

        while lo <= hi:

            mid = lo + (hi - lo) // 2
            hours_needed = 0

            for p in piles:
                hours_needed += math.ceil(p / mid)

            if hours_needed <= h:
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return res


        