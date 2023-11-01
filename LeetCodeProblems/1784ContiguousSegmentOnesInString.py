class Solution:
    def checkOnesSegment(s):
        contiguousStr = False
        enumStr = list(enumerate(s));
        endIndex = enumStr[-1][0]
        for i, c in enumStr:
            if (i+1 == endIndex):
                if (c == "1" and s[i+1] == "1"):
                    contiguousStr = True
                break
            if (c == "1" and s[i+1] == "1"):
                contiguousStr = True

        return contiguousStr

s1 = "1001"

answer1 = Solution.checkOnesSegment(s1)

print(answer1)

s2 = "110"

answer2 = Solution.checkOnesSegment(s2)

print(answer2)