from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        res = 0
        moves = [[1,0], [-1, 0], [0, 1], [0, -1]]

        def bfs(x, y):

            queue = deque()

            queue.append([x,y])
            grid[y][x] = "0"

            while queue:

                currX, currY = queue.popleft()

                for dx, dy in moves:

                    newX = currX + dx
                    newY = currY + dy

                    if not (0 <= newX < len(grid[0])) or not (0 <= newY < len(grid)):
                        continue

                    if grid[newY][newX] == "1":
                        grid[newY][newX] = "0"

                        queue.append([newX, newY])

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    bfs(x, y)
                    res += 1

        return res

                    




            
        