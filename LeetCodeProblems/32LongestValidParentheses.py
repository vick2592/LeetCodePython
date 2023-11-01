class Solution:
    def longestValidParentheses(s):
        longestStr = 0
        for x in range(len(s)):
            tempCount = 0 
            nextChar = "("
            for y in range(x, len(s)):
                if s[y] != nextChar:
                    if tempCount > longestStr:
                        longestStr = tempCount
                    tempCount = 0
                    nextChar = "("
                    continue
                tempCount += 1
                if nextChar == "(":
                    nextChar = ")"
                else:
                    nextChar = "("

        return longestStr

s = ")()())"
answer = Solution.longestValidParentheses(s)

print(answer)