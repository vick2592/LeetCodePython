class Solution:
    def getDistances(arr):
        intervals = []
        for i in range(len(arr)):
            cur = arr[i]
            count = 0
            for j in range(len(arr)):
                if i == j:
                    continue
                if arr[j] == cur:
                    count += (abs(i - j))

            intervals.append(count)

        return intervals


arr = [2,1,3,1,2,3,3]
answer = Solution.getDistances(arr)
print(answer)