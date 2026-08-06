from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        maxArea = 0

        moves = [[1,0], [-1, 0], [0, 1], [0,-1]]

        def bfs(row, col):

            currArea = 1

            queue = deque()
            queue.append([row, col])
            grid[row][col] = 0

            while queue:

                currRow, currCol = queue.popleft()

                for dr, dc in moves:

                    newRow = currRow + dr
                    newCol = currCol + dc

                    if not (0 <= newRow < len(grid)) or not (0<= newCol < len(grid[0])):
                        continue

                    if grid[newRow][newCol] == 1:
                        currArea += 1
                        grid[newRow][newCol] = 0
                        queue.append([newRow,newCol])

            return currArea

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, bfs(row,col))

        return maxArea







        