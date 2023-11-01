from copy import deepcopy

class Solution:
    def triangularSum(nums):
        numsCopy = deepcopy(nums)
        if(len(nums) == 1):
            return nums[0]
        while(True):
            newNums = []
            for i in range(len(numsCopy)):
                if i == len(numsCopy) - 1:
                    break
                newN = (numsCopy[i] + numsCopy[i+1]) % 10
                newNums.append(newN)
            if(len(newNums) == 1):
                return newNums[0]
            numsCopy = deepcopy(newNums)
            
nums = [1,2,3,4,5]
answer = Solution.triangularSum(nums)
print(answer)