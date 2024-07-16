class Solution:
    def diStringMatch(s):
        n = len(s)
        ans = [0] * (n + 1)
        l = 0
        h = n
        for i in range(n):
            if i == n-1:
                if s[i] == "I":
                    ans[i] = l
                    ans[i+1] = h
                else:
                    ans[i] = h
                    ans[i+1] = l
            if s[i] == "I":
                ans[i] = l
                l += 1
            else:
                ans[i] = h
                h -= 1

        return ans
    

s = "IDID"
# s = "III"
answer = Solution.diStringMatch(s)
print(answer)  # Output: [0,4,1,3,2]