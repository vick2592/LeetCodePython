class Solution:
    def findClosestElements(arr, k, x):
        answer = []
        xPos = -1
        for i in range(len(arr)):
            if arr[i] == x:
                xPos = i+1
                break
        if xPos == -1:
            if arr[0] > x:
                return sorted(arr[:k])
            elif arr[-1] < x:
                return sorted(arr[-k:])
        else:
            if xPos <= k:
                return sorted(arr[:k])
            elif xPos > k:
                lpos = xPos - k
                rpos = lpos + k
                return sorted(arr[lpos:rpos])

arr = [1,2,3,4,5]
k = 4
x = 3

arr = [1,1,2,3,4,5]
k = 4
x = -1

# arr = [1, 2, 3, 10, 20]
# k = 3
# x = 3

# arr = [1, 2, 3, 4, 10]
# k = 3
# x = 4

answer = Solution.findClosestElements(arr, k, x)
print(answer)  # Expected output: [1,2,3,4]