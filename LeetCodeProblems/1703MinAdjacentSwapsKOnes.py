class Solution:
    def minMoves(nums, k):
        distances = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                distances.append(count)
                count = 0
            else: 
                count += 1
        distances = sorted(distances)
        print(distances)
        minC = 0
        for j in range(k):
            minC += distances[j]


        return minC

nums = [1,0,0,0,0,0,1,1]
k = 3

[1,1,0,1]
k = 2

# nums = [1,0,0,1,0,1]
# k = 2
answer = Solution.minMoves(nums, k)

print(answer)  # Expected output: 3