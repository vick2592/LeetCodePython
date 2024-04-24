from copy import deepcopy

class Solution:
    def minimumSeconds(nums):
        allP = []
        tracker = {}
        nSize = len(nums)
        for i in nums:
            if tracker.get(i, 0):
                tracker[i] += 1
            else:
                tracker[i] = 1
        print(tracker)
        maxF = 0
        maxK = 0
        for k,v in tracker.items():
            if v > maxF:
                maxF = v
                maxK = k
        print(maxF, maxK)
        for n in range(len(nums)):
            tempList = []
            tempList.append(nums[n])
            if nums[(n-1+nSize) % nSize] not in tempList:
                tempList.append(nums[(n-1+nSize) % nSize])
            if nums[(n+1) % nSize] not in tempList:
                tempList.append(nums[(n+1) % nSize])
            allP.append(tempList)
        print(allP)
        count = 0
        while (len(allP) > 0):
            temp = 0
            test = deepcopy(allP)
            for i in range(len(test)):
                if maxK in test[i]:
                    allP.pop(i-temp)
                    temp += 1
                elif (maxK in test[(i-1+nSize) % nSize]):
                    allP[i-temp].append(maxK)
                elif (maxK in test[(i+1) % nSize]):
                    allP[i-temp].append(maxK)
                else:
                    continue
            print(allP)
            count += 1
            
        return count
    
nums = [2,1,3,3,2]
print(Solution.minimumSeconds(nums)) # 2