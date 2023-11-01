import math

class Solution:
    def maxAlternatingSum(nums):
        ans = 0
        direction = 'down'
        n = len(nums)
        for i in range(n-1):
            if direction == 'down' and nums[i] >= nums[i+1]:
                ans += nums[i]
                direction = 'up'
            elif direction == 'up' and nums[i] <= nums[i+1]:
                ans -= nums[i]
                direction = 'down'
        if direction == 'up':
            return ans
        return ans + nums[-1]

nums = [6,2,1,2,4,5]

print(Solution.maxAlternatingSum(nums))