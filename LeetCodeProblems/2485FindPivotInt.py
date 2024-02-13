class Solution:
    def pivotInteger(n):
        for x in range(1, n):
            countX = 0
            countY = 0
            for cx in range(1, x+1):
                countX += cx
            for cy in range(x,n+1):
                countY += cy
            print(countX, countY)
            if countX == countY:
                return x
        
        return -1
    
n = 8
ans = Solution.pivotInteger(n)
print(ans)