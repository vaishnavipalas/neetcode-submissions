class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        '''
        inputs: 
        - nums - array of distinct ints
        - target - int

        output:
        list of all unique combinations of nums where the numbers in the combination sum to exactly target

        - can reuse numbers
        - combinations are the same if they consist of the same frequency of chosen numbers
        - can return in any order
        '''

        res =[]

        def dfs(i, curr, remain):
            nonlocal res

            if remain == 0:
                res.append(curr.copy())
                return

            if remain < 0:
                return
            
            if i >= len(nums):
                return

            for i in range(i, len(nums)):

                curr.append(nums[i])
                dfs(i, curr, remain - nums[i])
                curr.pop()

            return

        curr = []

        dfs(0, curr, target)

        return res

            

        