class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = set()
        q = deque()

        moves = [[1,0], [-1,0], [0,1], [0,-1]]

        for r in range(num_rows):
            for c in range(num_cols):

                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r,c))

        dist = 0
        while q:

            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist

                for dr, dc in moves:

                    new_row = r + dr
                    new_col = c + dc

                    if new_row < 0 or new_row >= num_rows:
                        continue
                    elif new_col < 0 or new_col >= num_cols:
                        continue
                    elif grid[new_row][new_col] == -1:
                        continue
                    elif (new_row,new_col) in visited:
                        continue
                    else:
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))

            dist += 1


        
        