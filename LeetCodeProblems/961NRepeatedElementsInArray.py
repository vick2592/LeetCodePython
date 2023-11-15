class Solution:
    def repeatedNTimes(nums):
        n = len(nums)/2
        for num in nums:
            if nums.count(num) == n:
                return num
        return 0
    
nums = [5,1,5,2,5,3,5,4]
answer = Solution.repeatedNTimes(nums)

print(answer)