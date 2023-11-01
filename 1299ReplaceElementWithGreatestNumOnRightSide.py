import math

class Solution:
    def replaceElements(arr):
        temp = []
        for i in range(len(arr)):
            if i == len(arr)-1:
                    temp.append(-1)
                    break
            temp.append(max(arr[i+1:]))

        return temp

arr = [17,18,5,4,6,1]
answer = Solution.replaceElements(arr)
print(answer)