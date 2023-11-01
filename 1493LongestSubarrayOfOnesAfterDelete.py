from copy import deepcopy

class Solution:
    def longestSubarray(nums):
        print(nums)
        numsEnum = list(enumerate(nums))
        endIndex = numsEnum[-1][0]
        zeroIndex = []
        for i, n in numsEnum:
            if (n == 0):
                zeroIndex.append(i)
        #Base Case
        if (len(zeroIndex) == 0):
            return len(nums)-1

        longestOnesDict = {}
        longestOnesCount = 0
        for z in zeroIndex:
            listCopy = deepcopy(nums)
            listCopy.pop(z)
            numsCopy = list(enumerate(listCopy))
            print(numsCopy)
            onesCount = 1
            for ind, num in numsCopy:
                #End Case
                if (ind + 1 == endIndex-1):
                    if (num == 1 and numsCopy[ind + 1][1] == 1):
                        onesCount += 1
                        if(longestOnesCount < onesCount):
                            longestOnesCount = onesCount
                            longestOnesDict[z] = longestOnesCount
                        longestOnesDict[z] = onesCount
                        break
                    if (num == 1 and numsCopy[ind + 1][1] == 0):
                        if(longestOnesCount < onesCount):
                            longestOnesCount = onesCount
                            longestOnesDict[z] = longestOnesCount
                            break
                        longestOnesDict[z] = onesCount
                        break
                    if(num == 0 and numsCopy[ind + 1][1] == 1):
                        onesCount = 1
                        if(longestOnesCount < onesCount):
                            longestOnesCount = onesCount
                            longestOnesDict[z] = longestOnesCount
                            break
                        #longestOnesDict[z] = onesCount
                        break
                    if(num == 0 and numsCopy[ind + 1][1] == 0):
                        if(longestOnesCount < onesCount):
                            longestOnesCount = onesCount
                            longestOnesDict[z] = longestOnesCount
                            break
                        break
                #Loop Case
                if (num == 1 and numsCopy[ind + 1][1] == 1):
                    onesCount += 1
                    continue
                if (num == 1 and numsCopy[ind + 1][1] == 0):
                    #print("The oneCount is: ", onesCount)
                    if(longestOnesCount < onesCount):
                        #onesCount += 1
                        longestOnesCount = onesCount
                        longestOnesDict[z] = longestOnesCount
                        print("The longestCount is: ", longestOnesCount)
                        continue
                    continue
                if (num == 0 and numsCopy[ind + 1][1] == 0):
                    onesCount = 1
                    if(longestOnesCount < onesCount):
                        longestOnesCount = onesCount
                        longestOnesDict[z] = longestOnesCount
                    else: 
                        longestOnesDict[z] = onesCount
                    continue
                if (num == 0 and numsCopy[ind + 1][1] == 1):
                    onesCount = 1
                    continue

        return longestOnesCount

nums = [0,1,1,1,0,1,1,0,1]
answer = Solution.longestSubarray(nums);

print(answer)