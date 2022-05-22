class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        while row >= 0:
            if matrix[row][0] <= target:
                return target in matrix[row]
            else:
                row -= 1
        return False

    '''
    # Binary Search
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0])
        left, right = 0, w * h - 1
        while left <= right:
            mid = (left + right) // 2

            i = mid // w
            j = mid % w
            if matrix[i][j] > target:
                right = mid -1
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                return True
        return False
    '''