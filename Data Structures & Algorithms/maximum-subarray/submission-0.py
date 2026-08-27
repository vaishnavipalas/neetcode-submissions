class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        if not nums:
            return -1

        max_sum = nums[0]
        window_sum = 0

        for r in range(len(nums)):
            window_sum += nums[r]

            max_sum = max(max_sum, window_sum)

            if window_sum < 0:
                window_sum = 0

        return max_sum


        