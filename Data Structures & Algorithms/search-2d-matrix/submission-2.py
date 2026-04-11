class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        flattened = []
        for row in matrix:
            for num in row:
                flattened.append(num)
        
        left = 0
        right = len(flattened) - 1

        while left <= right:
            mid = (right + left) // 2
            if flattened[mid] == target:
                return True
            elif target > flattened[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
             
