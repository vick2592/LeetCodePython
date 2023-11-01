class Solution:
    def rotate(nums, k):
        lastIndex = len(nums)-1
        for i in range(k):
            test = nums[-1]
            nums.pop(lastIndex)
            nums.insert(0, test)
        #"""
        #Do not return anything, modify nums in-place instead.
        #"""
        print(nums)

nums = [1,2,3,4,5,6,7]

k = 3

Solution.rotate(nums, k)
print(nums)