class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        curr = set()
        m = 0

        left = 0

        for right in range(len(s)):


            while s[right] in curr and left < len(s):
                curr.remove(s[left])
                left += 1

            curr.add(s[right])
            m = max(m, len(curr))

        return m

        