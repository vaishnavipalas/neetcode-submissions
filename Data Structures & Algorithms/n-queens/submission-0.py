class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["." for _ in range(n)] for _ in range(n)]
        res = []

        def is_valid(row, col):

            for c in range(col):
                if board[row][c] == 'Q':
                    return False

            r, c = row - 1, col - 1

            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1

            r, c = row + 1, col - 1
            while r < n and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r += 1
                c -= 1

            return True


        
        def dfs(col):

            if col == n:
                res.append(["".join(r) for r in board])
                return

            for row in range(n):

                if is_valid(row,col):
                    board[row][col] = 'Q'

                    dfs(col + 1)

                    board[row][col] = '.'


            return

        dfs(0)

        return res





