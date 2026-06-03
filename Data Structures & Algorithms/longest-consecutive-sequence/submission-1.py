class Solution: 
    def longestConsecutive(self, nums: List[int]) -> int: 
        if not nums:
            return 0
        s = sorted(set(nums))

        longest = 1
        curr = 1

        for i in range(1, len(s)):
            if s[i-1] + 1 == s[i]:
                curr += 1
            else:
                longest = max(longest, curr)
                curr = 1

        return max(longest, curr)
        