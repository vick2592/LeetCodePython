class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        def helper(x, y):
            if x == m - 1 and y == n - 1:
                return grid[x][y]
            if x >= m or y >= n:
                return float('inf')
            if dp[x][y] != float('inf'):
                return dp[x][y]
            dp[x][y] = grid[x][y] + min(helper(x+1, y), helper(x, y+1))
            return dp[x][y]
        return helper(0, 0)
    
grid = [[1,3,1],[1,5,1],[4,2,1]]
ans = Solution()
print(ans.minPathSum(grid))  # Output: 7
    