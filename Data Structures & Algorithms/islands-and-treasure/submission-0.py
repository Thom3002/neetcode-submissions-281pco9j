class Solution:
    
    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        
        if not grid:
            return None

        n_rows, n_cols = len(grid), len(grid[0])

        def bfs(row, col):
            visited = set()
            queue = collections.deque()
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            queue.append((row, col))
            visited.add((row, col))
            dist = 1

            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        row = r + dr
                        col = c + dc
                        if row in range(0, n_rows) and col in range(0, n_cols) and grid[row][col] != -1 and (row, col) not in visited:
                            if grid[row][col] == 0:
                                return dist
                            else:
                                visited.add((row, col))
                                queue.append((row, col))
                dist += 1 
        # 1 -1  0  1
        # 1  1  1 -1
        # 1 -1  1 -1
        # 0 -1  1  1
            return -1

        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == INF:
                    grid[row][col] = bfs(row, col)
                else:
                    continue
        



