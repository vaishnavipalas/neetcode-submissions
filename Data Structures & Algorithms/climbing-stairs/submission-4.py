class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}

        def dfs(n):

            if n <= 2:
                return n

            ans= 0

            if (n-1) not in cache:
                cache[n-1] = dfs(n-1)

            if (n-2) not in cache:
                cache[n-2] = dfs(n-2)

            return cache[n-1] + cache[n-2]


        return dfs(n)
        