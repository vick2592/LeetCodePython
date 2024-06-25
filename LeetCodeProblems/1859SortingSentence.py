class Solution:
    def sortSentence(s):
        s = s.split()
        s.sort(key = lambda x: x[-1])
        print(s)
        for i in range(len(s)):
            s[i] = s[i][:-1]
        test = ""
        for j in s:
            test+=j
            test+=" "
        return test

s = "is2 sentence4 This1 a3"
ans = Solution.sortSentence(s)
print(ans)