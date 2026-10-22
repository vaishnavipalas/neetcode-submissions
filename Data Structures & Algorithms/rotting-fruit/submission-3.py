class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        moves = [(0,1), (1,0), (0,-1), (-1,0)]

        def empty(row,col):
            return grid[row][col] == 0

        def fresh(row,col):
            return grid[row][col] == 1

        def rotten(row,col):
            return grid[row][col] == 2

        q = deque()
        num_fresh = 0

        for r in range(ROWS):
            for c in range(COLS):

                if rotten(r,c):
                    q.append((r,c))
                elif fresh(r,c):
                    num_fresh += 1


        res = 0

        while q and num_fresh > 0:
            level = len(q)
            print(q)

            for i in range(level):
                row, col = q.popleft()

                for dr,dc in moves:
                    if not (0<=row+dr<ROWS) or not (0<=col+dc<COLS):
                        continue

                    if fresh(row+dr,col+dc):
                        q.append((row+dr, col+dc))
                        grid[row+dr][col+dc] = 2
                        num_fresh -=1

            res += 1


        return res if num_fresh == 0 else -1


                    



        

        