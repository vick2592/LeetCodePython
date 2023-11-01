class Solution:
    def twoSum(nums, target):
        ansewr = []
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target:
                    ansewr.append(x)
                    ansewr.append(y)
                    return ansewr

        return 0

nums = [2,7,11,15]
target = 9

answer = Solution.twoSum(nums, target)
print(answer)