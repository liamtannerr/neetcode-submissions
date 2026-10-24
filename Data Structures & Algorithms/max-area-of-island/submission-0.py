class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        res = 0

        n = len(grid)
        m = len(grid[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or (i, j) in visited or grid[i][j] == 0:
                return
            self.area += 1
            visited.add((i, j))
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 or (i, j) in visited:
                    continue
                self.area = 0
                dfs(i,j)
                res = max(res, self.area)
                

        return res
        