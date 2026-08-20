class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = set()
        q = deque()

        moves = []

        for r in range(num_rows):
            for c in range(num_cols):

                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r,c))

        def addRoom(r, c):
            if r < 0 or r >= num_rows:
                return
            if c < 0 or c >= num_cols:
                return
            if grid[r][c] == -1:
                return
            if (r,c) in visited:
                return

            visited.add((r,c))
            q.append((r,c))

        dist = 0
        while q:

            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist

                addRoom(r+1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c-1)

            dist += 1


        
        