class Solution:
    def maxScore(s):
        maxCount = 0
        for n in range(1, len(s)):
            fp = s[:n]
            sp = s[n:]
            zc = 0
            oc = 0
            for i in fp:
                if i == "0":
                    zc += 1
            for j in sp:
                if j == "1":
                    oc += 1
            if (zc + oc) > maxCount:
                maxCount = (zc + oc)
        
        return maxCount

s = "011101"
ans = Solution.maxScore(s)
print(ans)