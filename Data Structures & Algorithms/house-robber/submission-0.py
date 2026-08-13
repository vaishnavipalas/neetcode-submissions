class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = {}

        def dfs(i):

            if i >= len(nums):
                return 0
            
            if i == len(nums) - 1:
                return nums[i]

            if i + 2 not in cache:
                cache[i+2] = dfs(i+2)

            if i + 1 not in cache:
                cache[i+1] = dfs(i+1)

            return max(nums[i] + cache[i+2], cache[i+1])


        return dfs(0)

        