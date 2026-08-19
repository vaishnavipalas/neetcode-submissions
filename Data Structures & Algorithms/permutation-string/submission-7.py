from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        counts_s1 = Counter(s1)

        counts_s2 = Counter('')

        l = 0

        for r in range(len(s2)):
            counts_s2[s2[r]] += 1

            while counts_s2[s2[r]] > counts_s1[s2[r]]:
                counts_s2[s2[l]] -= 1
                l += 1
            
            if (r - l + 1) == len(s1):
                return True

        return False
        