class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # multi source bfs
        # first add all the rotten fruits to the queue
        # start the minute at 0
        # from each rotten fruit run a layer of bfs
        # -- if there is a fresh fruit (unvisited), make it rotten
        # -- add it to the queue
        # increment the minute after the entire layer of bfs


        num_rows, num_cols = len(grid), len(grid[0])
        # visited = set()
        q = deque()
        moves = [(1,0), (-1, 0), (0, 1), (0,-1)]
        fresh_count = 0

        for row in range(num_rows):
            for col in range(num_cols):

                if grid[row][col] == 2:
                    q.append((row,col))
                    # visited.add((row,col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        minute = 0

        while q and fresh_count > 0:

            for i in range(len(q)):

                curr_row, curr_col = q.popleft()

                for dr, dc in moves:

                    new_row = curr_row + dr
                    new_col = curr_col + dc

                    if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 1:
                        fresh_count -= 1
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))

            minute += 1

        return minute if fresh_count == 0 else -1
        