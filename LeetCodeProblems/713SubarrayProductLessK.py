class Solution:
    def numSubarrayProductLessThanK(nums, k):
        ans = []
        test = []
        for x in range(len(nums)):
            cur = []
            for y in range(x, len(nums)):
                cur.append(nums[y])
                test.append(tuple(cur))
        for t in test:
            prod = 1
            for n in t:
                prod *= n
            if prod < k:
                ans.append(t)
             
                
        return len(ans)
    

nums = [10,5,2,6]
k = 100

answer = Solution.numSubarrayProductLessThanK(nums, k)
print(answer)
