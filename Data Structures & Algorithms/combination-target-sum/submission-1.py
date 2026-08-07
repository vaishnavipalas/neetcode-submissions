class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        curr = []


        def backtrack(start_idx, remain):

            if remain == 0:
                res.append(curr.copy())
                return
            
            if remain < 0:
                return


            for j in range(start_idx, len(nums)):

                curr.append(nums[j])

                backtrack(j, remain - nums[j])

                curr.pop()

        backtrack(0, target)
        return res
        