class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        num = 0
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return

            if (i, j) in visited:
                return

            if grid[i][j] == "0":
                return
                
            visited.add((i, j))
            
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    num += 1
                    dfs(i, j)

        return num