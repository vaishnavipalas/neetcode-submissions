class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows

        for row in board:
            seen = set()
            for box in row:
                if box in seen and box != ".":
                    return False
                else:
                    seen.add(box)
        
        # check columns
        for c in range(9):
            seen = set()
            for r in range(9):
                box = board[r][c]
                if box in seen and box != ".":
                    return False
                else:
                    seen.add(box)

        # check boxes

        def helper(i, j):
            seen = set()
            for x in range(i, i+3):
                for y in range(j, j+3):
                    box = board[x][y]
                    if box in seen and box != '.':
                        return False
                    else:
                        seen.add(box)
            return True

        for i in range(3):
            for j in range(3):
                if not helper(i*3,j*3):
                    return False
        
        return True

        