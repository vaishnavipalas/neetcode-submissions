class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        '''
        understand -
        you are able to replace at most k characters in the string
        given that want to return the longest substring of the same character

        match - 
        sliding window

        implement -
        init result to -1
        edge case - if empty, return 0
        init left pointer

        keep a dict of all the curr substring and the frequencies of each character
        each time we increment the right pointer, find the char with highest freq
        subtract that frequency from the length of the subtring, 
        if it is less than k we can make k replacements
        if not, then shrink the window by moving left pointer
        update the result int if the length is bigger

        return the result at the end
        '''

        ans = -1
        freqs = dict()
        l = 0

        if not s:
            return 0
        
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1

            highest = max(freqs.values())

            if (r - l + 1) - highest > k and l < r:
                freqs[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)

        return ans
        