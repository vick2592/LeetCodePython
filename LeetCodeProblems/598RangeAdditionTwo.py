class Solution:
    def maxCount(m, n, ops):
        dp = [[0 for i in range(n)] for j in range(m)]
        if len(ops) == 0:
            return m*n
        for i in range(len(ops)):
            xP = ops[i][0]
            yP = ops[i][1]
            for j in range(xP):
                for k in range(yP):
                    dp[j][k] += 1
                    
        print(dp)
        highest = max([max(i) for i in dp])
        count = 0
        for i in dp:
            for j in i:
                if j == highest:
                    count += 1
        return count
    
m = 3
n = 3
ops = [[2,2],[3,3]]
ans = Solution.maxCount(m, n, ops)
print(ans) #4
        