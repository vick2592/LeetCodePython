class Solution:
    def arrangeCoins(n):
        count = 0
        nCount = 0
        i = 1
        while (nCount + i < n):
            nCount += i
            i += 1
            count += 1
            
        return count
    
    
n = 8
ans = Solution.arrangeCoins(n)
print(ans)