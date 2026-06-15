class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == '':
            return ''
        window = {}
        t_freqs = {}
        for x in t:
            t_freqs[x] = t_freqs.get(x, 0) + 1

        have = 0
        need = len(t_freqs)

        result = (-1,-1)
        res_len = float('inf')
        left = 0

        for right in range(len(s)):

            window[s[right]] = window.get(s[right], 0) +1

            if s[right] in t_freqs and window[s[right]] == t_freqs[s[right]]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    result = (left, right)
                    res_len = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in t_freqs and window[s[left]] < t_freqs[s[left]]:
                    have -=1  

                left += 1   

        l, r = result
        return s[l:r+1] if res_len != float('inf') else ''




            

        



        