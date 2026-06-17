from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_freqs = Counter(s1)
        s2_freqs = Counter(s2[:len(s1)])

        if s1_freqs == s2_freqs:
            return True

        left = 0
        right = len(s1)

        while right < len(s2):
            s2_freqs[s2[right]] += 1

            s2_freqs[s2[left]] -= 1
            if s2_freqs[s2[left]] == 0:
                s2_freqs.pop(s2[left])

            if s2_freqs == s1_freqs:
                return True

            left += 1
            right += 1

        return False