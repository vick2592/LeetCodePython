class Solution:
    def minimumBoxes(n):
        r = n % 3
        q = n - r
        print(q)
        tri = 3
        while q > 0:
            if q - tri == 0:
                return tri
            q -= tri
            tri *= 2
        return 0
    
n = 10
answer = Solution.minimumBoxes(n)
print(answer)