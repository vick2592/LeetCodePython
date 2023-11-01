class Solution:
    def constrainedSubsetSum(nums, k):
        numsLen = len(nums)
        maxSum = max(nums)
        #print(maxSum)
        for i in range(numsLen):
            tempList = []
            prevJ = i
            for j in range(i, numsLen):
                if(j != prevJ):
                    continue
                if(prevJ == numsLen - 1):
                    tempList.append(nums[j])
                    break
                tempSum = -9999999
                tempList.append(nums[j])
                for testK in range(1, k+1):
                    if((j + testK) > numsLen-1):
                        break
                    curSum = nums[j] + nums[j+testK]
                    print("Current j and testK is: ", j, testK)
                    #print("Current nums[j] and nums[j+k] values are: ", nums[j], nums[j+testK])
                    print("The current sum is: ",curSum)
                    if (curSum > tempSum):
                        tempSum = curSum
                        prevJ = j+testK
                        print("Current tempSum and prevJ is: ", tempSum, prevJ)

            print("Current tempList is: ", tempList)
            testSum = 0
            for num in tempList:
                testSum += num
            if testSum > maxSum:
                maxSum = testSum
        return maxSum

nums = [10,-2,-10,-5,20]
k = 2

answer = Solution.constrainedSubsetSum(nums, k)
print("The max sum is: ", answer)

