class Solution:
    def mirrorReflection(p, q):
         while (p % 2 == 0 and q % 2 == 0): p, q = p / 2, q / 2
         return 1 - p % 2 + q % 2

answer = Solution.mirrorReflection(3,2)
print(answer)