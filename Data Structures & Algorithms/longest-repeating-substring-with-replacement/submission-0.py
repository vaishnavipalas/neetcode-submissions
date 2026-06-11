class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxi = 0
        left = 0
        max_freq = 0
        freqs = dict()

        for right in range(len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1

            max_freq = max(max_freq, freqs[s[right]])

            while (right - left + 1) - max_freq > k:

                freqs[s[left]] -= 1
                left += 1

            maxi = max(maxi, right - left + 1)

        return maxi



        