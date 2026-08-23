class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][0]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                return True

        if target >= matrix[bottom][0]:
            top = bottom
     
        left = 0
        right = len(matrix[top]) - 1

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[top][mid]:
                left = mid + 1
            elif target < matrix[top][mid]:
                right = mid - 1
            else:
                return True 

        return False