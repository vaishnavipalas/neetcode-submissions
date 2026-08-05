class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        curr = []
        seen = set()

        def backtrack():

            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for j in range(len(nums)):

                if nums[j] in seen:
                    continue

                seen.add(nums[j])

                curr.append(nums[j])

                backtrack()

                curr.pop()
                seen.remove(nums[j])

        backtrack()
        return res


        