from functools import cache
from itertools import permutations

class Solution:
    def rearrangeSticks(n, k):
        #DP solution
        @cache
        def dp(n,k):
            if n == k:
                return 1
            if k == 0:
                return 0
            return (dp(n-1, k-1) + (n-1) * dp(n-1, k)) % (10**9 + 7)
        return dp(n,k)
        #My Solution initially with combination that took to long.
        # count = 0
        # nList = list(range(1, n+1))
        # for x in permutations(nList, n):
        #     curTall = 0
        #     currC = 0
        #     for y in x:
        #         if y > curTall:
        #             curTall = y
        #             currC += 1
        #     if currC == k:
        #         count += 1
                    
        # mod = 10**9+7        
        # return count % mod
    
n = 3
k = 2
n = 20
k = 11
ans = Solution.rearrangeSticks(n, k)
print(ans)