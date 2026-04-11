class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N_ROWS = 9
        N_COLUMNS = 9
        
        def is_valid_quadrant(quadrant: List[str]) -> bool:
            values = set()
            for val in quadrant:
                if val == '.':
                    continue
                elif int(val) >= 1 and int(val) <= 9:
                    if val not in values:
                        values.add(val)
                    else:
                        return False
                    continue
                else:
                    return False
            return True

                    
            return True
        
        def get_quadrants(board: List[List[str]]) -> List[List[str]]:
            quadrants = [[]*N_COLUMNS for _ in range(N_ROWS)]
            for i in range(N_ROWS):
                for j in range(N_COLUMNS):
                    quad_idx = get_quadrant_idx(i, j)
                    quadrants[quad_idx].append(board[i][j])

            return quadrants

        def get_quadrant_idx(i: int, j: int) -> int:
            if i <= 2: # 0, 1, 2 quadrants
                if j <= 2:
                    return 0
                elif j <= 5:
                    return 1
                elif j <= 8:
                    return 2
            elif i <= 5: # 3, 4, 5 quadrants
                if j <= 2:
                    return 3
                if j <= 5:
                    return 4
                if j <= 8:
                    return 5
            elif i <= 8: # 6, 7, 8 quadrants
                if j <= 2:
                    return 6
                if j <= 5:
                    return 7
                if j <= 8:
                    return 8
            else:
                return -1
            

                  
        
        for i in range(9):
            values = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in values:
                    values.add(board[i][j])
                else:
                    return False

        for i in range(9):
            values = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] not in values:
                    values.add(board[j][i])
                else:
                    return False


        quadrants = get_quadrants(board)
        for quadrant in quadrants:
            if not is_valid_quadrant(quadrant):
                return False


        return True

