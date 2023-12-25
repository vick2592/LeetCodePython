class Solution:
    def numOfPairs(nums, target):
        validInd = []
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if (nums[x] + nums[y] == target):
                    if((x,y) not in validInd):
                        validInd.append((x,y))
                if (nums[y] + nums[x] == target):
                    if((y,x) not in validInd):    
                        validInd.append((y,x))
                        
        print(validInd)
        return len(validInd)
    
nums = ["123","4","12","34"]
target = "1234"
nums = ["1","1","1"]
target = "11"

answer = Solution.numOfPairs(nums, target)
print(answer)