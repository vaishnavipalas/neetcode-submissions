class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if len(s) <= 1:
            return len(s)

        curr = {s[0]}
        maxL = 1
        left = 0
        
        for right in range(1, len(s)):
            while s[right] in curr:
                curr.remove(s[left])
                left += 1
            
            curr.add(s[right])
            maxL = max(maxL, len(curr))
        
        return maxL


        

        
