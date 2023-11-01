class Solution:
    def findFinalValue(nums, original):
        while (original in nums):
            original *= 2
        return original
nums = [5,3,6,1,12]
original = 3

answer = Solution.findFinalValue(nums, original)

print(answer)
