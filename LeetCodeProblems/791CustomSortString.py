class Solution:
    def customSortString(order, s):
        answer = ""
        for c in order:
            if c in s:
                answer += c
        print(answer)

        for i in range(len(answer), len(s)):
            answer += s[i]
        return answer

order = "cbafg"
s = "abcd"

answer = Solution.customSortString(order, s)
print(answer)