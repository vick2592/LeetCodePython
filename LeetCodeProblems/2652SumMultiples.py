class Solution:
    def sumOfMultiples(n):
         ans = []
         for i in range(1, n+1):
             if i % 3 == 0 or i % 5 == 0 or i% 7 == 0:
                 ans.append(i)
         return sum(ans)
   

answer = Solution.sumOfMultiples(10)
print(answer)