class Solution:
    def numDecodings(self, s: str) -> int:

        '''
        recursion - top down memoization

        check substring of length 1 or 2 is in the range 1 to 26
        '''
        n = len(s)
        memo = {}


        def recurse(i):

            if i == n:
                return 1

            if s[i] == '0':
                return 0

            if i in memo:
                return memo[i]

            res = 0

            res += recurse(i+1)

            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                res += recurse(i+2)

            memo[i] = res

            return res


        return recurse(0)


        