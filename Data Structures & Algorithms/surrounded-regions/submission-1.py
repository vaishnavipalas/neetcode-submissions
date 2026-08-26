class Solution:
    def solve(self, board: List[List[str]]) -> None:

        num_rows = len(board)
        num_cols = len(board[0])

        def dfs(row, col):

            if not (0<= row < num_rows) or not (0<= col < num_cols):
                return

            if board[row][col] != "O":
                return
            
            board[row][col] = "#"

            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row + 1, col)
            dfs(row - 1, col)
        
        # first go through the borders
        for r in range(num_rows):
            dfs(r, 0)
            dfs(r, num_cols-1)
        for c in range(num_cols):
            dfs(0, c)
            dfs(num_rows-1, c)

        for r in range(num_rows):
            for c in range(num_cols):

                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"




        