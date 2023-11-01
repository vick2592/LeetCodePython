from copy import deepcopy

class Solution:
    def minMoves(nums, limit):
        minMoves = 0
        #Create a function that checks im array nums is complementary
        def isComplimentary(numList):
            isCompliment = True
            value = numList[0] + numList[len(numList)-1]
            for i in range(len(numList)):
                if(i == len(numList)/2):
                    break
                if(numList[i] + numList[len(numList) - 1 - i] != value):
                    isCompliment = False

            return isCompliment
        #Base case check
        testBase = isComplimentary(nums)
        if(testBase == True):
            return 0

        tupList = []
        tupListV2 = []
        for j in range(len(nums)):
            if(j == len(nums)/2):
                break
            tupList.append((nums[j], nums[len(nums)-1-j], nums[j] + nums[len(nums)-1-j]))
            tupListV2.append((j, len(nums)-1-j, nums[j] + nums[len(nums)-1-j]))
        tupList = sorted(tupList, key = lambda x: x[2], reverse = True)
        tupListV2 = sorted(tupListV2, key = lambda x: x[2], reverse = True)
        print("TupList is: ", tupList)
        print("TupListV2 is: ", tupListV2)      
        valueCount = {}
        for itm in tupList:
            if(itm[2] not in valueCount.keys()):
                valueCount[itm[2]] = 1
                continue
            valueCount[itm[2]] += 1

        print("ValueCount is: ", valueCount)
        loopList = list(valueCount.items())
        loopList = sorted(loopList, key = lambda x: x[1], reverse = True)
        print(loopList)
        maxVal = limit*2
        for v, c in loopList:
            if(v/(2*limit) > 1):
                continue
            maxVal = v
            break

        print("Current Max val is: ", maxVal)
        tempNums = deepcopy(nums)
        while(isComplimentary(tempNums) == False):
            for i1,i2,i3 in tupListV2:
                if i3 != maxVal:
                    diff = maxVal - i3
                    print(maxVal, diff, i1, i2, i3, (tempNums[i2] + diff)/limit)
                    if (tempNums[i1] + diff)/limit > 1:
                        if(tempNums[i2] + diff)/limit > 1:
                            tempNums[i1] = maxVal-1
                            tempNums[i2] = 1
                            minMoves += 2
                        else: 
                            tempNums[i2] = maxVal - tempNums[i1]
                            minMoves += 1
                    else:
                        tempNums[i1] = maxVal - tempNums[i2]
                        minMoves += 1
                        
        return minMoves

nums = [1,2,4,3]
limit = 4
nums = [1,2,2,1]
limit = 2
answer = Solution.minMoves(nums, limit)

print(answer)