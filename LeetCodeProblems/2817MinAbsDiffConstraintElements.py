class Solution:
    def minAbsoluteDifference(nums, j):
        minNum = float('inf')
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if abs(y - x) >= j:
                    if abs(nums[x] - nums[y]) <= minNum:
                        minNum = abs(nums[x] - nums[y])
        return minNum

nums = [5,3,2,10,15]
x = 1
answer = Solution.minAbsoluteDifference(nums, x)
print(answer)