class Solution:
    def countSubstrings(s, t):
        count = 0
        for i in range(len(s)):
            for j in range(len(t)):
                diff = 0
                for k in range(min(len(s) - i, len(t) - j)):
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff == 1:
                        count += 1
                    if diff == 2:
                        break
        return count
    
s = "aba"
t = "baba"
        
ans = Solution.countSubstrings(s, t)
print(ans)