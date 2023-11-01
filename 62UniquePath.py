from functools import cache
from itertools import product

class Solution:
    def uniquePathsMemoise(m, n):
        @cache
        def dfs(i, j):
            if i >= m or j >= n:      return 0
            if i == m-1 and j == n-1: return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)

    def uniquePathsTabulation(m, n):
        dp = [[1]*n for i in range(m)]
        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
m = 3
n = 7

answer = Solution.uniquePathsMemoise(m,n)
print(answer)

answer2 = Solution.uniquePathsTabulation(m,n)
print(answer2)