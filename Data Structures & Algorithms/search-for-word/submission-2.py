class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visted = set()

        def backtrack(x, y, i):

            if i == len(word):
                return True

            if (not 0 <= x < len(board)) or (not 0 <= y < len(board[0])) or (x,y) in visted or (board[x][y] != word[i]) :
                return False

            visted.add((x, y))
            for dx, dy in moves:

                if backtrack(x+dx, y+dy, i+1):
                    return True

            visted.remove((x, y))

            return False
                    

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row,col,0):
                    return True
        return False

        