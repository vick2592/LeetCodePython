class Solution:
    def xorOperation(n, start):
        nList = []
        for i in range(n):
            nList.append(start + 2*i)
        ans = 0
        for i in nList:
            ans ^= i
        return ans
n = 5
start = 0
print(Solution.xorOperation(n, start)) #8

