class Solution:
    def maxFreq(s, maxLetters, minSize, maxSize):
        subStr = []
        for x in range(len(s)):
            for y in range(x+1,len(s)):    
                subStr.append(s[x:y+1])
        print(subStr)
        testStr = []
        for i in range(len(subStr)):
            if len(subStr[i]) >= minSize and len(subStr[i]) <= maxSize:
                testStr.append(subStr[i])
        print(testStr)
        strDict = {}
        for i in range(len(testStr)):
            if testStr[i] not in strDict:
                strDict[testStr[i]] = 1
            else:
                strDict[testStr[i]] += 1
        print(strDict)
        greatest = 0
        for k, v in strDict.items():
            if v > greatest:
                greatest = v
        return greatest
    
s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4
print(Solution.maxFreq(s, maxLetters, minSize, maxSize)) #2