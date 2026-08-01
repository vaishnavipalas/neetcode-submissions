class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        curr = []

        candidates.sort()

        def dfs(start_idx, remain):

            if remain == 0:
                res.append(curr.copy())
                return

            if remain < 0:
                return 

            for j in range(start_idx, len(candidates)):

                if j > start_idx and candidates[j] == candidates[j-1]:
                     continue

                curr.append(candidates[j])

                dfs(j + 1, remain - candidates[j])

                curr.pop()

        dfs(0, target)
        return res
        