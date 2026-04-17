class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            visited.add((i, j))
            area = 1

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(0, rows) and c in range(0, cols) and (r, c) not in visited and grid[r][c] == 1:
                        queue.append((r, c))
                        visited.add((r, c))
                        area += 1
            
            return area



        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, bfs(i, j))
        
        return max_area