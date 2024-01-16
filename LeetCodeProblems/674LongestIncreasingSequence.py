class Solution:
    def findLengthOfLCIS(nums):
        count = 0
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[y] > nums[x]:
                    continue
                else:
                    if y > count:
                        count = y
                        break
                    
        return count
nums = [1,3,5,4,7]
answer = Solution.findLengthOfLCIS(nums)
print(answer)
