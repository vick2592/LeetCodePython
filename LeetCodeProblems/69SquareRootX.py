class Solution:
    def mySqrt(x):
        count = 1
        while(count * count <= x):
            count += 1
        return count-1
    
x = 8
answer = Solution.mySqrt(x)
print(answer)

