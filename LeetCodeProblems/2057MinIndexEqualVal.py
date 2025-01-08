class Solution:
    def smallestEqual(nums):
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                print(i)
                print(nums[i])
                print(i % 10)   
                return i
        return -1

nums = [4,3,2,1]
ans = Solution.smallestEqual(nums)
print(ans) # 3

