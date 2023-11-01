import math

class Solution:
    def findBestValue(arr, target):
        if(sum(arr) == target):
            print("Sum is equal to target in array allready so int is the max.")
            return max(arr)
        numc = math.ceil(target/len(arr))
        numf = math.floor(target/len(arr))
        if(abs(numc*len(arr) - target)<abs(numf*len(arr) - target)):
            num = numc
        else:
            num = numf

        if(num <= min(arr)):
            print("The average int is the min.")
            return num


        return num
arr = [4,3,5]
target = 10
answer = Solution.findBestValue(arr,target)
print(answer)