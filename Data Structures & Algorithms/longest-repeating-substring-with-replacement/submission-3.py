class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts= dict()
        longest_sub = 0
        max_freq = 0


        l= 0

        for r in range(len(s)):

            if s[r] in counts:
                counts[s[r]] += 1
            else:
                counts[s[r]] = 1

            max_freq = max(max_freq, counts[s[r]])

            while (r - l +1) - max_freq > k and l < r:
                if counts[s[l]] > 0:
                    counts[s[l]] -= 1
                l += 1
            
            longest_sub = max(longest_sub, r - l +1)


        return longest_sub

            

        