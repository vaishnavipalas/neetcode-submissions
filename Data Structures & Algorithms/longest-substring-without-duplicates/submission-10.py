class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        longest = 0
        curr = set()


        for r in range(len(s)):


            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            curr.add(s[r])
            if r - l + 1 > longest:
                longest = r - l + 1

        return longest


        