class Solution:
    def reformat(s):
        numList = []
        letterList = []
        for n in range(len(s)):
            if s[n] in ['0','1','2','3','4','5','6','7','8','9']:
                numList.append(s[n])
            else:
                letterList.append(s[n])
        print(numList, letterList)
        if len(numList) - len(letterList) == 0:
            testStr = ""
            for i in range(len(numList)):
                testStr += numList[i]
                testStr += letterList[i]
            return testStr
        elif  abs(len(numList) - len(letterList)) == 1:
            if (len(numList) > len(letterList)):
                testStr = ""
                testStr.append(numList[0])
                for i in range(len(letterList)):
                    testStr += letterList[i]
                    testStr += numList[i+1]
                return testStr
            else:
                testStr = ""
                testStr.append(letterList[0])
                for i in range(len(numList)):
                    testStr += numList[i]
                    testStr += letterList[i+1]
                return testStr
        else:
            return ""

s = "a0b1c2"

answer = Solution.reformat(s)
print(answer)