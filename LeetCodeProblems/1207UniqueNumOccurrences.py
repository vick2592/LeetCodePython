class Solution:
    def uniqueOccurrences(arr):
        ans = True
        numDict = {}
        for n in arr:
            numDict[n] = numDict.get(n, 0) + 1
        for i in list(numDict.keys()):
            if list(numDict.values()).count(numDict[i]) > 1:
                ans = False
                break
        print(numDict)
        return ans
    
arr = [1,2,2,1,1,3]
arr = [1,2]
answer = Solution.uniqueOccurrences(arr)
print(answer)