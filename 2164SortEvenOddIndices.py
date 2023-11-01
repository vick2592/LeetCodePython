class Solution:
    def sortEvenOdd(nums):

        enumNums = list(enumerate(nums))
        print(enumNums)
        #Sort the odd numbers in decreasing order

        for i in range(len(enumNums)):
            for j in range(len(enumNums)):
                if(i%2!=0 and j%2!=0 and i!=j):
                    if(i<j):
                        if(nums[i]<nums[j]):
                            tempI =  nums[i]
                            tempJ = nums[j]
                            nums[j] = tempI
                            nums[i] = tempJ
                            continue
                    if(nums[i]>nums[j]):

                        tempI =  nums[i]
                        tempJ = nums[j]
                        nums[j] = tempI
                        nums[i] = tempJ
                        continue

        #Sort the even numbers in increasing order
        for i in range(len(enumNums)):
            for j in range(len(enumNums)):
                if(i%2==0 and j%2==0 and i!=j):
                    if(i<j):
                        if(nums[i]>nums[j]):
                            tempI =  nums[i]
                            tempJ = nums[j]
                            nums[j] = tempI
                            nums[i] = tempJ
                            continue
                    if(nums[i]<nums[j]):

                        tempI =  nums[i]
                        tempJ = nums[j]
                        nums[j] = tempI
                        nums[i] = tempJ
                        continue
        print(nums)
        return nums

nums = [4,1,2,3]
answer = Solution.sortEvenOdd(nums)
print(answer)