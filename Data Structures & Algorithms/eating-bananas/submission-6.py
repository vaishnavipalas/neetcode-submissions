class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        '''
        [1,2,3,4]
        hours = 9
        num piles = 4

        min_eating_rate = 1
        max_eating_rate = 4

        1/4 -> 1
        2/4 -> 1
        3/4 -> 1
        4/4 ->1
        '''


        min_rate = 1
        max_rate = max(piles)

        lo, hi = min_rate, max_rate

        def find_total(k):
            total = 0

            for i in piles:
                total += math.ceil(i/k)

            return total


        while lo < hi:

            mid = lo + (hi-lo) // 2

            total = find_total(mid)
            print(total)

            if total > h:
                lo = mid + 1
            else:
                hi = mid


        return lo



        