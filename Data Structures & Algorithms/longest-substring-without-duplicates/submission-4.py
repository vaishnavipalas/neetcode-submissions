class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
        understand -
        input - string
        output - int
        a substring is a segment of characters within the input in consecutive order
        want to return the longest one that has no duplicates
        constraints - should be o(n) time
        edge case - empty string


        match - sliding window

        implement -
        init a max so far to -1
        init a left pointer
        progress through the string incrementing the right one at a time while
        the invariant holds.
        as soon as there is a duplicate move the left pointer until the duplicate is gone
        keep track of duplicates by keeping a set
        '''

        if not s:
            return 0
        ans = -1
        l = 0
        substring = set()

        for r in range(len(s)):
            curr = s[r]
            if curr not in substring:
                substring.add(curr)
            else:
                while curr in substring and l < r:
                    substring.remove(s[l])
                    l += 1
                substring.add(curr)
            
            ans = max(ans, len(substring))
        
        return ans



        