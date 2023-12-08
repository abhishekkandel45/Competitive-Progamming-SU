class Solution:
    # Function to find the distance of nearest cell having 1 in the grid for each cell.
    def nearest(self, grid):
        # Code here
        m = len(grid)
        n = len(grid[0])
        ans = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans[i][j] = 0
                else:
                    ans[i][j] = float('inf')
        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    ans[i][j] = min(ans[i][j], ans[i-1][j] + 1)
                if j-1 >= 0:
                    ans[i][j] = min(ans[i][j], ans[i][j-1] + 1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i+1 < m:
                    ans[i][j] = min(ans[i][j], ans[i+1][j] + 1)
                if j+1 < n:
                    ans[i][j] = min(ans[i][j], ans[i][j+1] + 1)
        return ans
