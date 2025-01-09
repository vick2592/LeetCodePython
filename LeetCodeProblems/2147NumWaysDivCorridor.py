class Solution:
    def numberOfWays(self, corridor):
        SCount = 0
        for i in corridor:
            if i == 'S':
                SCount += 1
        if SCount % 2 != 0 or SCount == 0:
            return 0
        elif SCount // 2 == 1:
            return 1
        s = 0
        p = 0
        result = 1
        for c in corridor:
            if c == 'S':
                s += 1
                if s == SCount:
                    break
                if p > 0:
                    result *= (p+1)
                    p = 0
            elif s > 0 and s % 2 == 0:
                p += 1

        return result % (10**9 + 7)

corridor = "SSPPSPS"
# corridor = "PPSPSP"
# corridor = "PPSPSPSSPPSPS"
corridor = "SSPPSPSPPSPSP"
sol = Solution()
ans = sol.numberOfWays(corridor)
print(ans)  # 4