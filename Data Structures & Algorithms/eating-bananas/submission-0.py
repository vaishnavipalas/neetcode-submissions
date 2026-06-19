import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hours_needed(k):
            hours= 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours
        
        
        maxk = max(piles)

        lo = 1
        hi = maxk
        result = hi
        
        while lo <= hi:

            mid = lo + (hi - lo) // 2
            if hours_needed(mid) <=h:
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return result

