class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        num_rows = len(heights)
        num_cols = len(heights[0])

        moves = [[1,0], [-1, 0], [0, 1], [0, -1]]

        pacific = set()
        atlantic = set()

        def dfs(row, col, ocean):
            ocean.add((row, col))

            for dr, dc in moves:
                if (row + dr, col + dc) in ocean:
                    continue

                if not (0 <= row + dr < num_rows) or not (0 <= col + dc < num_cols):
                    continue

                if heights[row + dr][col + dc] >= heights[row][col]:
                    ocean.add((row + dr, col + dc))
                    dfs(row + dr, col + dc, ocean)

        for r in range(num_rows):
            for c in range(num_cols):

                if r == 0 or c == 0:
                    dfs(r, c, pacific)
                if r == num_rows - 1 or c == num_cols - 1:
                    dfs(r, c, atlantic)


        return [[r,c] for r,c in pacific & atlantic]

                

            
        