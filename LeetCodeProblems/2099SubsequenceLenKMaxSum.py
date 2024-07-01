class Solution:
    def maxSubsequence(nums, k):
        numsCopy = sorted(nums, reverse=True)
        print(numsCopy)
        ansList = numsCopy[:k]
        return ansList
    

nums = [-1,-2,3,4]
k = 3

ans = Solution.maxSubsequence(nums, k)
print(ans)