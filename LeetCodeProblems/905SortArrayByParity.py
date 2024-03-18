class Solution:
    def sortArrayByParity(nums):
        even = []
        odd = []
        for n in nums:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        
        numsSort = even + odd
        return numsSort
    
nums = [3,1,2,4]
ans = Solution.sortArrayByParity(nums)
print(ans)  # Output: [2,4,3,1]

        