class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest = 0

        for num in nums:
            if (num - 1) in s:
                continue
            else:
                curr = 1
                while (num + curr) in s:
                    curr += 1
                longest = max(curr, longest)

        return longest

        