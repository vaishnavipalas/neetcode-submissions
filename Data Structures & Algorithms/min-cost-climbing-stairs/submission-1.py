class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}

        def dfs(i):

            if i >= len(cost):
                return 0

            if i+1 not in cache:
                cache[i+1] = dfs(i+1)
            if i+2 not in cache:
                cache[i+2] = dfs(i+2)

            return cost[i] + min(cache[i+1], cache[i+2])

        return min(dfs(0), dfs(1))
        