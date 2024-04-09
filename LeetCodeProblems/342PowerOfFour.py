class Solution:
    def isPowerOfFour(n):
        while n > 1:
            n /= 4
            if n == 1:
                return True
        return False
    
n = 16
print(Solution.isPowerOfFour(n))