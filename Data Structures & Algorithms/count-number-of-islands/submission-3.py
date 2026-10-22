class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        num_islands = 0


        def dfs(row,col):

            if not (0<=row<ROWS) or not (0<=col<COLS):
                return

            if grid[row][col] == '0':
                return

            grid[row][col] = '0'
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

            return


        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r,c)

        return num_islands
        