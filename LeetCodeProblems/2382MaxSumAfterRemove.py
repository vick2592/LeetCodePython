from copy import deepcopy

class Solution:
    def maximumSegmentSum(nums, removeQueries):
        newArray = []
        clone = deepcopy(nums)
        for i in removeQueries:
            clone[i] = 0
            test1 = sum(clone[:i])
            test2 = sum(clone[i+1:])
            if test1 > test2:
                newArray.append(test1)
            else:
                newArray.append(test2)
        
        return newArray
    
nums = [1,2,5,6,1]
removeQueries = [0,3,2,4,1]
ans = Solution.maximumSegmentSum(nums, removeQueries)
print(ans)

        