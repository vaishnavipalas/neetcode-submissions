class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_prod = nums[0]
        curr_max, curr_min = nums[0], nums[0]

        for i in range(1, len(nums)):

            curr_max, curr_min= (
                max(nums[i], curr_max * nums[i], curr_min * nums[i]),
                min(nums[i], curr_max * nums[i], curr_min * nums[i])
            )

            max_prod = max(max_prod, curr_max, nums[i])

        return max_prod
        