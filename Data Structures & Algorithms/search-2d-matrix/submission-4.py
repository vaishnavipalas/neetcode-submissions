class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False
        
        m = len(matrix)
        n = len(matrix[0])

        lo = 0
        hi = m * n - 1

        while lo <= hi:

            mid = lo + (hi - lo) // 2
            row = (mid) // n
            col = (mid) % n
            print(matrix[row][col])

            if matrix[row][col] < target:
                lo = mid + 1
            elif matrix[row][col] > target:
                hi = mid - 1
            else:
                return True

        return False
