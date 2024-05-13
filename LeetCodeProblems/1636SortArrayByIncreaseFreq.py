class Solution:
    def frequencySort(nums):
        numMap = {}
        for i in nums:
            if i in numMap:
                numMap[i] += 1
            else:
                numMap[i] = 1
        print(numMap)
        ans = sorted(numMap.items(), key = lambda x: (x[1], -x[0]))
        return ans

nums = [2,3,1,3,2]
print(Solution.frequencySort(nums)) #[1,3,3,2,2]