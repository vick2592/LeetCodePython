from math import pow

class Solution:
    def __init__(self):
        self.grid = []
        self.k = 0

    def numberOfPaths(self, grid, k):
        self.grid = grid
        self.k = k
        m = len(grid)
        n = len(grid[0])
        dp = [[[-1] * k for _ in range(n)] for _ in range(m)]

        def helper(i, j, s, m, n, k, grid, dp):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return (s + grid[i][j]) % k == 0
            if dp[i][j][s] != -1:
                return dp[i][j][s]
            else:
                dp[i][j][s] = (helper(i + 1, j, (s + grid[i][j]) % k, m, n, k, grid, dp) + helper(i, j + 1, (s + grid[i][j]) % k, m, n, k, grid, dp)) % (pow(10, 9) + 7)
                return dp[i][j][s]

        return helper(0, 0, 0, m, n, k, grid, dp)

grid = [[5,2,4],[3,0,5],[0,7,2]]
grid2 = [[3,7],[2,1]]
k = 3

answer = Solution()
print(answer.numberOfPaths(grid,k))
print(answer.numberOfPaths(grid2,k))