import math
from itertools import combinations

class Solution:
    def maximumTastiness(price, k):
        #Get all combinations and then save them to a dictionary with value being minimum absolute difference
        combDict = {}
        enumPrice = list(enumerate(price))
        endIndex = enumPrice[-1][0]

        combinationList = list(combinations(price, k))
        #print(combinationList)

        for comb in combinationList:
            combPair = list(combinations(comb, 2))
            #print(combPair)
            pairList = []
            for pair in combPair:
                taste = abs(pair[0] - pair[1])
                pairList.append(taste)

            minValue = min(pairList)
            combDict[comb] = minValue
            #print(comb)
            #print(pairList) 
            #print("The minimum value of given pairList is: ", combDict[comb])

        answerDict = {}

        for k,v in combDict.items():
            #print(k)
            #print(v)
            keySum = 0
            for i in k:
                keySum += i
            answerDict[keySum] = v

        answerDict = sorted(answerDict.items(), key=lambda x: (x[1],x[0]), reverse=True)

        print(answerDict)
        answer = answerDict[0][1]
        #print(first_item)
        return answer

price = [13,5,1,8,21,2]
k = 3

answer = Solution.maximumTastiness(price, k)
print(answer)

