class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False
        
        m = len(matrix)
        n = len(matrix[0])

        lo = 0
        hi = m * n - 1

        mid = lo + (hi - lo) // 2
        row = (mid + 1) // n
        col = (mid + 1) % m
        print(row)
        print(col)

        # while lo <= hi:

        #     mid = lo + (hi - lo) // 2
        #     row = (mid + 1) // n
        #     col = (mid + 1) % m
        #     print(row)
        #     print(col)

        #     if matrix[row][col] < target:
        #         lo = row * col
        #     elif matrix[row][col] > target:
        #         hi = row * col
        #     else:
        #         return True

        # return False
