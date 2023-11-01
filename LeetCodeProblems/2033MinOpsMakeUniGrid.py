class Solution:
    def minOperations(grid, x):
        numList = []
        for tempX in grid:
            for y in tempX:
                numList.append(int(y))
                
        numList.sort()
        print(numList)
        for n in range(len(numList)):
            temp =  numList[n]
            #print(type(temp))
            #print(temp%x)
            if ((temp%x) != 0):
                return -1
            
        median = numList[int(len(numList)/2)]
        count = 0
        for t in numList:
            while t != median:
                if t > median:
                    t -= x
                else:
                    t += x
                count += 1
        return count
    
grid = [[2,4],[6,8]]
x = 2
        
answer = Solution.minOperations(grid, x)
print(answer)
