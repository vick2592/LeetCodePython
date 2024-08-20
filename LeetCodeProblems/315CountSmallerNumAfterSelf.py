class Solution:
    def countSmaller(nums):
        n = len(nums)
        res = []
        for i in range(n):
            count = 0
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    count += 1
            res.append(count)
        return res

nums = [5,2,6,1]
answer = Solution.countSmaller(nums)
print(answer)  # Expected output: [2,1,1,0] 