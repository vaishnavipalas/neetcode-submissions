class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        '''
        return possible permutations
        '''

        res = []

        def dfs(curr, chosen):

            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):

                if chosen[i]:
                    continue

                curr.append(nums[i])
                chosen[i] = True
                dfs(curr, chosen)
                chosen[i] = False
                curr.pop()

            return

        curr =[]
        chosen = [False] * len(nums)

        dfs(curr, chosen)

        return res
        