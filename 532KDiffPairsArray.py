import math

class Solution:
    def findPairs(nums, k):
        #Loop through the array pushing the current number and index upto the end - 1 index. From there keep track of all pairs generated 

        enumNums = list(enumerate(nums))
        endIndex = enumNums[-1][0]
        uniquePairs = []
        numsSize = len(nums)

        #print(enumNums)
        #test = abs(3-5)
        #print("The absolute test is: ", test)

        for i, n in enumNums:
            if i+1 == endIndex:
                #End of loop execution statement
                if n >= 0 and i+1 < numsSize:
                    if n != nums[i+1]:
                        if (abs(n - nums[i+1]) == k):
                            if ((n, nums[i+1]) in uniquePairs):
                                break
                            uniquePairs.append((n,nums[i+1]))
                break
            for j in range(i+1,endIndex + 1):
                print("The n value is: ", n)
                print("The j value is: ", nums[j])
                if j == endIndex:
                    if n >= 0 and j < numsSize:
                        if n != nums[j]:
                            if (abs(n - nums[j]) == k):
                                if ((n, nums[j]) in uniquePairs):
                                    break
                                uniquePairs.append((n, nums[j]))
                    break
                if n >= 0 and j < numsSize:
                    if n != nums[j]:
                        if (abs(n - nums[j]) == k):
                            if ((n, nums[j]) in uniquePairs):
                                continue
                            uniquePairs.append((n, nums[j]))

        print(uniquePairs)
        answer = len(uniquePairs)
        return answer

nums = [3,1,4,1,5]
k = 2

answer = Solution.findPairs(nums, k)

print(answer)


#0 <= i, j < nums.length
#i != j
#nums[i] - nums[j] == k
