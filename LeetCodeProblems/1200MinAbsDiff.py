class Solution:
    def minimumAbsDifference(arr):
        arr.sort()
        min_diff = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))
        return [[arr[i], arr[i + 1]] for i in range(len(arr) - 1) if arr[i + 1] - arr[i] == min_diff]

    
arr = [4,2,1,3]
ans = Solution.minimumAbsDifference(arr)
print(ans)  # Output: [[1,2],[2,3],[3,4]]
