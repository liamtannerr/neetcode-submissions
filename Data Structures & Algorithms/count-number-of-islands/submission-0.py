class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        res = 0
        seen = set()
        n = len(grid)
        m = len(grid[0])

        def dfs(idx):
            i, j = idx
            if i < 0 or j < 0 or i >= n or j >= m or idx in seen or grid[i][j] == "0":
                return

            seen.add((i,j))
            dfs((i, j + 1))
            dfs((i, j - 1))
            dfs((i + 1, j))
            dfs((i - 1, j))

            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0" or (i,j) in seen:
                    continue
                res += 1
                dfs((i,j))

        return res

