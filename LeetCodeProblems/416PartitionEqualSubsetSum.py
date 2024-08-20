class Solution:
    def canPartition(nums):
        subArrays = []
        subVal = {}
        def recusriveArray(arr):
            if len(arr) == 0:
                return
            if arr not in subArrays:
                subArrays.append(arr)
            for i in range(0, len(arr)):
                recusriveArray(arr[:i] + arr[i + 1:])

        recusriveArray(nums)
        print(subArrays)
        for k in range(len(subArrays)):
            subVal[k] = sum(subArrays[k])
        print(subVal)
        vals = [v for v in subVal.values()]
        for v in vals:
            if vals.count(v) > 1:
                return True
        return False

nums = [1,5,11,5]
answer = Solution.canPartition(nums)
print(answer)  # Expected output: True