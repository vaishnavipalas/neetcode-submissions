class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def recurse(i):

            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(recurse(i-1), nums[i] + recurse(i-2))
            return memo[i]


        return recurse(len(nums)- 1)
        