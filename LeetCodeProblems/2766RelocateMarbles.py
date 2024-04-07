class Solution:
    def relocateMarbles(nums, moveFrom, moveTo):
        for i in range(len(moveFrom)):
            ind = nums.index(moveFrom[i])
            nums[ind] = moveTo[i]
            
        nums = sorted(nums)
        return nums
    
nums = [1,6,7,8]
moveFrom = [1,7,2]
moveTo = [2,9,5]

ans = Solution.relocateMarbles(nums, moveFrom, moveTo)
print(ans)  # Output: [2, 6, 9, 8]