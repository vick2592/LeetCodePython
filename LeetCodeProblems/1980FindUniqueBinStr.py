class Solution:
    def findDifferentBinaryString(nums):
        numLen = len(nums[0])
        bStart = f'{0:0{numLen}b}'
        start = 0
        test = f'{start:0{numLen}b}'
        while(len(test) <= numLen):
            print(test)
            if test not in nums:
                return test
            start += 1
            test = f'{start:0{numLen}b}'

        return ""
    
nums = ["01","10"]
answer = Solution.findDifferentBinaryString(nums)
print(answer)
