class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []
        n = len(nums)

        def backtrack(i):

            res.append(curr.copy())

            for j in range(i, len(nums)):

                curr.append(nums[j])
                backtrack(j+1)
                curr.pop()


            return

        backtrack(0)

        return res

            
        