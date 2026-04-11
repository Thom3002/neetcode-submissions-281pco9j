class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        num_islands = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            queue = collections.deque()
            queue.append((row, col))
            visited.add((row, col))

            while queue:
                row, col = queue.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols)) and grid[r][c] == "1" and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))
            
                    
        for i in range(rows):
            for j in range(cols): 
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    num_islands += 1
        
        return num_islands
