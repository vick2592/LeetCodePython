class Solution:
    def minimumChanges(s, k):
        def ChangesForSemiPalindrom(l, r):
            n = r - l + 1
            ans = 1000000000
            for f in fact[n]:
                len = n // f
                change = 0
                for part in range(f):
                    for i in range(len // 2):
                        if s[l + i * f + part] != s[l + (len - i - 1) * f + part]:
                            change += 1
                ans = min(ans, change)
            return ans

        def MinChange(ind, k):
            if ind == n:
                return 0 if k == 0 else 1000000000
            if k == 0:
                return 1000000000
            ans = dp[ind][k]
            if ans != -1:
                return ans
            ans = 1000000000
            for nxt in range(ind, n):
                ans = min(ans, changes[ind][nxt] + MinChange(nxt + 1, k - 1))
            return ans

        n = len(s)
        fact = [[] for _ in range(n + 1)]
        for j in range(1, n + 1):
            for i in range(j + j, n + 1, j):
                fact[i].append(j)
        changes = [[0] * n for _ in range(n)]
        for j in range(n):
            for i in range(j, n):
                changes[j][i] = ChangesForSemiPalindrom(j, i)

        dp = [[-1] * (k + 1) for _ in range(n)]
        return MinChange(0, k)

        
s = "abcac"
k = 2
answer = Solution.minimumChanges(s, k)
print(answer)  # Expected output: 1

