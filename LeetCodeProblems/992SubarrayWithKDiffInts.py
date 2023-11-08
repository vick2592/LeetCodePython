from copyreg import add_extension


class Solution:
    def subarraysWithKDistinct(nums, k):
        allCombs = []
        for x in range(len(nums)):
            for y in range(x, len(nums)+1):
                allCombs.append(nums[x:y])
        #print(allCombs)
        ansList = []
        for comb in allCombs:
            uniqueNums = []
            if len(comb) >= k:
                for c in comb:
                    if c not in uniqueNums:
                        uniqueNums.append(c)
                if len(uniqueNums) == k:
                    ansList.append(comb)
        return  len(ansList)
    
nums = [1,2,1,2,3]
k = 2
nums = [1,2,1,3,4]
k = 3
answer = Solution.subarraysWithKDistinct(nums, k)

print(answer)

