class Solution:
    def countGoodNumbers(n):
        odd = 5
        even = 4
        count = 1
        for i in range(n):
            if (i % 2 == 0):
                count *= odd
            else:
                count *= even

        mod = 10**9 + 7
        return count % mod
    

n = 50
print(Solution.countGoodNumbers(n)) # 400