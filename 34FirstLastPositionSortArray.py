class Solution:
    def searchRange(nums, target):
        TargetPositions = []
        for index, num in enumerate(nums):
            if num == target:
                TargetPositions.append(index)

        if (len(TargetPositions) == 0):
            return [-1,-1]

        return TargetPositions

nums = [5,7,7,8,8,10]
target = 6

nums.sort()
print(nums)

answer = Solution.searchRange(nums, target)

print(answer)