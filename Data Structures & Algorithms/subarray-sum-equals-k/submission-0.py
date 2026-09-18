class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        sum = 0

        hashmap = {
            0: 1
        }

        for i in range(len(nums)):

            sum += nums[i]

            if sum - k in hashmap:
                res += hashmap[sum-k]

            hashmap[sum] = hashmap.get(sum, 0) + 1

        return res
        