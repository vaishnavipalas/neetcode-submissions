class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if not nums:
            return 0


        dp = [0] * len(nums)


        dp[0] = [nums[0]]
        max_prod = nums[0]
        prev_max = nums[0]
        prev_min = nums[0]

        for i in range(1, len(nums)):

            prev_max, prev_min= max(nums[i], prev_max * nums[i], prev_min * nums[i]), min(nums[i], prev_max * nums[i], prev_min * nums[i])

            max_prod = max(max_prod, prev_max, prev_min, nums[i])

        return max_prod
        