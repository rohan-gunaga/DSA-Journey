class Solution(object):
    def searchMatrix(self, matrix, target):

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
                pass
            else:
                right = mid - 1
                pass

        return False




        