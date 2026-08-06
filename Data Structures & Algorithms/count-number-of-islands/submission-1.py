class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        res = 0

        moves = [[1,0], [-1,0 ], [0,1], [0,-1]]

        def dfs(row,col):

            if not grid:
                return

            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
                return

            if grid[row][col] == "0":
                return

            grid[row][col] = "0"

            for dr, dc in moves:

                dfs(row + dr, col + dc)

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == "1":
                    dfs(row, col)
                    res += 1

        return res

        