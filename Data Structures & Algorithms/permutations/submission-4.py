class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        '''
        return possible permutations
        '''

        res = []
        curr =[]
        chosen = [False] * len(nums)
        def dfs():

            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):

                if chosen[i]:
                    continue

                curr.append(nums[i])
                chosen[i] = True
                dfs()
                chosen[i] = False
                curr.pop()

            return

        dfs()

        return res
        