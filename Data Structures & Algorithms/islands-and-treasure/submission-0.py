class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        n = len(grid)
        m = len(grid[0])

        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i, j))

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        while queue:
            i, j = queue.popleft()

            for di, dj in directions:
                gi = i + di
                gj = j + dj

                if gi < 0 or gi >= n or gj < 0 or gj >= m or grid[gi][gj] != INF:
                    continue

                grid[gi][gj] = 1 + grid[i][j]
                queue.append((gi, gj))