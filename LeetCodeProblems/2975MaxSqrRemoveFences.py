class Solution:
    #My solution
    # def maximizeSquareArea(m, n, hFences, vFences):
    #     def helper(x, y):
    #         if x == y:
    #             return x ** 2
    #         return -1

    #     if n == m:
    #         return (n-1)*(m-1)
        
    #     minBase = -1
    #     for i in range(len(hFences)):
    #         for j in range(len(vFences)):
    #             if i + 1 < len(hFences):
    #                 minBase = max(minBase, helper(hFences[i+1], vFences[j]))
    #             if j + 1 < len(vFences):
    #                 minBase = max(minBase, helper(hFences[i], vFences[j+1]))
    #             if i + 1 < len(hFences) and j + 1 < len(vFences):
    #                 minBase = max(minBase, helper(hFences[i+1], vFences[j+1]))
    #             minBase = max(minBase, helper(hFences[i], vFences[j]))
    #     mod = 10**9+7        
    #     return minBase % mod
    #Leetcode solution
    def maximizeSquareArea(m, n, h, v):
        mod = 10**9 + 7
        s1, s2 = set(), set()
        h.extend([1, m])
        v.extend([1, n])
        h.sort()
        v.sort()

        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                s1.add(h[j] - h[i])

        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                s2.add(v[j] - v[i])

        ans = 0
        for i in s1:
            if i in s2:
                k = i * i
                ans = max(ans, k)

        if ans == 0:
            return -1
        return ans % mod
    
m = 4
n = 3
hFences = [2,3]
vFences = [2]
# m = 6
# n = 7
# hFences = [2]
# vFences = [4]
        
print(Solution.maximizeSquareArea(m, n, hFences, vFences)) #4