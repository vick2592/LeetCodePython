class Solution:
    def majorityElement(nums):
        majoritySize = len(nums)/2

        majorityDict = {}
        majorityDict[0] = 0
        majorityNum = 0

        for n in nums:
            majorityDict[n] = 0

        for i in nums:
            majorityDict[i] += 1
            if majorityDict[i] > majoritySize and majorityDict[majorityNum] < majorityDict[i]:
                majorityNum = i

        return majorityNum
        

nums = [2,2,1,1,1,2,2]

answer = Solution.majorityElement(nums)
print(answer)