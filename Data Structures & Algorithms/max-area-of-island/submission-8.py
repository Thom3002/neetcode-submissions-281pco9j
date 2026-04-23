class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        n_rows, n_cols = len(grid), len(grid[0])
        visited = set()


        def bfs(row, col):
            queue = collections.deque()
            queue.append((row, col))
            visited.add((row, col))
            area = 1

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] 

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(0, n_rows) and col in range(0, n_cols) and grid[row][col] == 1 and (row, col) not in visited:
                        queue.append((row, col))
                        visited.add((row, col))
                        area += 1

            return area


        for row in range(n_rows):
            for col in range(n_cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    max_area = max(max_area, bfs(row, col))

        return max_area
