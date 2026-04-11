class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        def get_matrix_idx(m: int, n: int, idx: int):
            return idx // n, idx % n
            # m = 3 
            # n = 4
            # 5
            # 5 % 3 = 1

        n = n_rows * n_cols
        # n = 12
        left = 0 
        right = n - 1 # 11
        while left <= right: # 0 <= 11
            mid = (left + right) // 2 # 11 // 2 = 5
            i, j = get_matrix_idx(n_rows, n_cols, mid) # 1, 1
            mid_num = matrix[i][j]
            if mid_num == target:
                return True
            elif mid_num > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
             
