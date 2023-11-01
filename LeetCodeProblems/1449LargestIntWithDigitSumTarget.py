from copy import deepcopy

class Solution:
    costList = []
    numberList = []
    def largestNumber(cost, target):
        costMap = []
        for n in range(len(cost)):
            costMap.append((n+1, cost[n]))
        costMap = sorted(costMap, key=lambda x: (x[1], -x[0]))
        print(costMap)
        recursiveList = []
        recursiveNumList = []
        Solution.recursiveCost(costMap, 0, recursiveList, recursiveNumList, target)
        print(Solution.costList)
        print(Solution.numberList)

        if(len(Solution.numberList) == 0):
            return "0"
        largestNum = 0
        for lst in Solution.numberList:
            tempLst = sorted(lst, reverse = True)
            print("Current tempLst is: ", tempLst)
            numStringList = []
            for n in tempLst:
                numStringList.append(str(n))
            tempNum = int("".join(numStringList))
            if tempNum > largestNum:
                largestNum = tempNum

        stringNum = str(largestNum)
        return stringNum

    def recursiveCost(costDict, level, curList, numberList, targetVal):
        copyList = deepcopy(curList)
        copyNumList = deepcopy(numberList)
        if level >= len(costDict):
            return 
        copyList.append(costDict[level][1])
        copyNumList.append(costDict[level][0])
        print(copyList)
        print(copyNumList)
        curSum = sum(copyList)
        print("Current sum is: ", curSum)
        if(curSum > targetVal):
            #print("True")
            #print("level: ", level )
            return
        if curSum == targetVal:
            Solution.costList.append(copyList)
            Solution.numberList.append(copyNumList)

        for i in range(9):
            Solution.recursiveCost(costDict, level + i, copyList, copyNumList, targetVal)

cost = [4,3,2,5,6,7,2,5,5]
target = 9
#cost = [2,4,6,2,4,6,4,4,4]
#target = 5
#cost = [7,6,5,5,5,6,8,7,8]
#target = 12
answer = Solution.largestNumber(cost,target)
print(answer)
