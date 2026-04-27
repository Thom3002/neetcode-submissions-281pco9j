import collections

class RestaurantGrid:
    def __init__(self, rows: int, cols: int) -> None:
        self.grid = [[0] * cols for _ in range(rows)]
        self.restaurants_count = 0
        return

    def addRestaurant(self, row: int, col: int) -> None:
        self.grid[row][col] = 1
        self.restaurants_count += 1
        return

    def hasRestaurant(self, row: int, col: int) -> bool:
        return self.grid[row][col] == 1

    def countRestaurants(self) -> int:
        return self.restaurants_count

    def bfs(self, i: int, j: int, visited: set) -> None:
        queue = collections.deque()
        queue.append((i, j))
        visited.add((i, j))


        n_rows = len(self.grid)
        n_cols = len(self.grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if row in range(n_rows) and col in range(n_cols) and (row, col) not in visited and self.grid[row][col] == 1:
                    visited.add((row, col))
                    queue.append((row, col))


    def countClusters(self) -> int:
        clusters = 0

        n_rows = len(self.grid)
        n_cols = len(self.grid[0])

        visited = set()

        for i in range(n_rows):
            for j in range(n_cols):
                if self.grid[i][j] == 1 and (i, j) not in visited:
                    self.bfs(i, j, visited)
                    clusters += 1

        return clusters




grid = RestaurantGrid(3, 3)
grid.addRestaurant(0, 0)
grid.addRestaurant(0, 1)
grid.addRestaurant(2, 2)

print(grid.hasRestaurant(0, 1))  # True
print(grid.countRestaurants())   # 3
print(grid.countClusters())      # 2
