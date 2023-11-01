import math

class Solution:
    def minimizeMax(nums, p):
        pairList = []
        indList = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                 if(i == j):
                     continue
                 if((i,j,abs(nums[i]-nums[j])) not in pairList and (j,i,abs(nums[i]-nums[j])) not in pairList):
                     pairList.append((i,j,abs(nums[i]-nums[j])))



        pairList = sorted(pairList, key = lambda x: x[2])
        answerList = []
        for item in pairList:
            if(item[0] not in indList and item[1] not in indList):
                indList.append(item[0])
                indList.append(item[1])
                answerList.append(item)
        print(answerList)
        print(pairList)
        return answerList[p-1][2]
nums = [10,1,2,7,1,3]
p = 2

answer = Solution.minimizeMax(nums, p)
print(answer)