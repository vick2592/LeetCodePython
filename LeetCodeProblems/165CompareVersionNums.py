class Solution:
    def compareVersion(version1, version2):
        ver1len = len(version1)
        ver2len = len(version2)
        revisionCount = 0
        previousN = 0
        revDict = {}
        version1revs = ["major1", "minor1", "patch1"]
        version2revs = ["major2", "minor2", "patch2"]
        for n in range(ver1len):
            if n == ver1len - 1:
                revDict[version1revs[revisionCount]] = version1[previousN:]
                break
            if(version1[n] == '.'):
                revDict[version1revs[revisionCount]] = version1[previousN:n]
                previousN = n+1
                revisionCount+=1
        revisionCount = 0
        previousN = 0
        for n in range(ver2len):
                if n == ver2len - 1:
                    revDict[version2revs[revisionCount]] = version2[previousN:]
                    break
                if(version2[n] == '.'):
                    revDict[version2revs[revisionCount]] = version2[previousN:n]
                    previousN = n+1
                    revisionCount+=1
        errorCorrect = 0
        for n in range(3):
            if(version1revs[n] not in revDict.keys()):
                revDict[version1revs[n]] = '0'
                continue
            for ind, c in list(enumerate(revDict[version1revs[n]])):
                if(ind == len(revDict[version1revs[n]]) + errorCorrect):
                    continue
                if(ind == 0 and len(revDict[version1revs[n]]) == 1):
                    continue
                if(ind - errorCorrect == 0 and c == '0'):
                    revDict[version1revs[n]] = revDict[version1revs[n]][ind + 1-errorCorrect:]
                    errorCorrect += 1
        errorCorrect = 0
        for n in range(3):
            if(version2revs[n] not in revDict.keys()):
                revDict[version2revs[n]] = '0'
                continue;
            for ind, c in list(enumerate(revDict[version2revs[n]])):
                if(ind == len(revDict[version2revs[n]]) + errorCorrect):
                    continue
                if(ind == 0 and len(revDict[version2revs[n]]) == 1):
                    continue
                if(ind - errorCorrect == 0 and c == '0'):
                    revDict[version2revs[n]] = revDict[version2revs[n]][ind + 1-errorCorrect:]
                    errorCorrect += 1
        for n in range(3):
            if(int(revDict[version1revs[n]]) > int(revDict[version2revs[n]])):
                return 1
            if(int(revDict[version1revs[n]]) == int(revDict[version2revs[n]])):
                continue
            return - 1
        print(revDict, revDict.keys())

        return 0

version1 = "001.1"
version2 = "10.1"
answer = Solution.compareVersion(version1,version2)
print(answer)