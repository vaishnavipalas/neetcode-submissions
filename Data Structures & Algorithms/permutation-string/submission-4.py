from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        '''
        understand -
        input - two strings: s1 and s2
        output - boolean

        if s1 is in s2 as a permutation, we return true
        else we return false
        can be in any order (permutation)
        must be consecutive (no chars in between)

        match - sliding window - fixed size

        implement -
        edge case: if len(s2) < len(s1), return false
        init left pointer
        keep track of the current window with a set - start with up to index len(s1)
        get the frequencies of s1 - goal is to compare them to each substring of
        s2 that we check to see if the permutation exists - use library
        iterate through s2 from len(s1)
        remove the left most, add the current char
        compare the frequencies
        if not equal, move on, otherwise return true

        if we go through the whole thing and can't match, then return false
        

        '''
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s2 < len_s1:
            return False

        freqs_s1 = Counter(list(s1))
        l = 0
        freqs_s2 = Counter(list(s2[l:len_s1-1]))

        for r in range(len_s1, len_s2):
            freqs_s2[s2[r]] += 1
            if freqs_s2 == freqs_s1:
                return True
            if s2[l] in freqs_s2 and freqs_s2[s2[l]] == 0:
                freqs_s2.pop(s2[l])

            freqs_s2[s2[l]] -= 1
            l += 1
        
        return False
        