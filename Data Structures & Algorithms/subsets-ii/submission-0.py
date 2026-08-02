class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []
        nums.sort()


        def dfs(start_idx):

            res.append(curr.copy())
            


            for j in range(start_idx, len(nums)):

                if j != start_idx and nums[j] == nums[j-1]:
                    continue

                curr.append(nums[j])
                dfs(j + 1)

                curr.pop()

        dfs(0)
        return res

            
        