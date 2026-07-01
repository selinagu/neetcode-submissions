class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        num = 0
        visited = set()

        def dfs(i, j):
            visited.add((i, j))
            if i - 1 >= 0 and (i-1, j) not in visited and grid[i-1][j] == "1":
                dfs(i - 1, j)
            if i + 1 < n and (i+1, j) not in visited and grid[i+1][j] == "1":
                dfs(i + 1, j)
            if j - 1 >= 0 and (i, j-1) not in visited and grid[i][j-1] == "1":
                dfs(i, j - 1)
            if j + 1 < m and (i, j+1) not in visited and grid[i][j+1] == "1":
                dfs(i, j + 1)
            return

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    num += 1
                    dfs(i, j)

        return num