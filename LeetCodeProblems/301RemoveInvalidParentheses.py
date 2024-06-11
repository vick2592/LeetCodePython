class Solution:
    def removeInvalidParentheses(s):
        return [s]
    
s = "(a)())()"
ans = Solution.removeInvalidParentheses(s)
print(ans) #["(a)()()", "(a())()"]
        