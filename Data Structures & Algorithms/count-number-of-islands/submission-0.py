class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        visited = set()

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for x, y in directions:
                    r, c = row + x, col + y
                    if  (r in range(rows) and c in range(cols)) and grid[r][c] == '1' and (r, c) not in visited:
                        visited.add((r, c))
                        queue.append((r, c)) 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    num_islands += 1
        
        return num_islands