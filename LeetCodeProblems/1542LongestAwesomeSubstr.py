class Solution:
    def longestAwesome(s):
        subStr = []
        for x in range(len(s)):
            for y in range(x, len(s)):
                if(s[x:y+1] not in subStr):
                    subStr.append(s[x:y+1])
        subStr = sorted(subStr, key = len, reverse = True)
        print(subStr)

        for sub in subStr:
            tempDict = {}
            for tempY in range(len(sub)):
                if sub[tempY] in tempDict.keys():
                    tempDict[sub[tempY]] += 1
                else:
                    tempDict[sub[tempY]] = 1  
                #print(tempDict)
            countSingles = 0
            for k,v in tempDict.items():
                if v % 2 == 0:
                    continue
                if v == 1:
                    countSingles += 1
            if (countSingles > 1):
                continue
            else:
                return len(sub)
        return 1
        
s = "3242415"
answer = Solution.longestAwesome(s)
print(answer)
        
