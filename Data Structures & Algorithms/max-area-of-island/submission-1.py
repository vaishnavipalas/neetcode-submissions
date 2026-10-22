class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        seen = set()

        def dfs(r, c):

            if r < 0 or c < 0:
                return 0

            if r >= ROWS or c >= COLS:
                return 0

            if grid[r][c] == 0:
                return 0

            if (r,c) in seen:
                return 0

            seen.add((r,c))
            area = 1
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area

        for row in range(ROWS):
            for col in range(COLS):
                a = dfs(row, col)
                res = max(res, a)


        return res

                




        
        
        