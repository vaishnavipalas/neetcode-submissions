from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        len_s1 = len(s1)

        if len(s2) < len_s1:
            return False
        counts_s1 = Counter(s1)
        counts_s2 = Counter(s2[0:len_s1])

        if counts_s1 == counts_s2:
            return True

        l = 0
        for r in range(len_s1, len(s2)):

            counts_s2[s2[r]] += 1
            counts_s2[s2[l]] -= 1
            l += 1

            if counts_s1 == counts_s2:
                return True

        return False




        
        