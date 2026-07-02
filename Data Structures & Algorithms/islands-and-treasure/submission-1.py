class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        n = len(grid)
        m = len(grid[0])

        def dfs(i, j, dist):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == -1 or grid[i][j] < dist:
                return

            grid[i][j] = dist
            dfs(i - 1, j, dist + 1)
            dfs(i + 1, j, dist + 1)
            dfs(i, j - 1, dist + 1)
            dfs(i, j + 1, dist + 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i, j, 0)