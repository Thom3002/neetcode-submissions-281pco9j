class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_area = 0
        
        n_rows, n_cols = len(grid), len(grid[0])
        visited = set()

        def bfs(row, col):
            curr_area = 1
            queue = collections.deque()
            queue.append((row, col))
            visited.add((row, col))
            
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(n_rows) and c in range(n_cols)) and grid[r][c] == 1 and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))
                        curr_area += 1

            return curr_area

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    curr_area = bfs(i, j)
                    max_area = max(curr_area, max_area)


        return max_area 