class Solution:
    def minimumTime(grid):
        xVal = len(grid)
        yVal = len(grid[0])
        highestStep = 0
        
        for x in range(xVal):
            for y in range(yVal):
                if grid[x][y] > highestStep:
                    highestStep = grid[x][y]
               
        step = 0
        answerDict = []
        stack = [(0,0,0)]
        while(len(stack) > 0):
            x, y, step = stack.pop(0)
            noStackAdded = True
            if x - 1 > 0 and grid[x-1][y] <= step + 1 and step + 1 <= highestStep:
                answerDict.append((x-1, y, step + 1))
                stack.append((x-1, y, step + 1))
                noStackAdded = False
            if x + 1 <= xVal-1 and grid[x+1][y] <= step + 1 and step + 1 <= highestStep:
                answerDict.append((x+1, y, step + 1))
                stack.append((x+1, y, step + 1))
                noStackAdded = False
            if y - 1 > 0 and grid[x][y-1] <= step + 1 and step + 1 <= highestStep:
                answerDict.append((x, y-1, step + 1))
                stack.append((x, y-1, step + 1))
                noStackAdded = False
            if y + 1 <= yVal-1 and grid[x][y+1] <= step + 1 and step + 1 <= highestStep:
                answerDict.append((x, y+1, step + 1))
                stack.append((x, y+1, step + 1))
                noStackAdded = False
               
            if noStackAdded == True:
                noEndPoint = True
                for i in answerDict:
                    if i[0] == xVal - 1 and i[1] == yVal - 1:
                        noEndPoint = False
                if noEndPoint == True:
                    return -1

        print(answerDict)
        minCount = 10**8
        for p in answerDict:
            if p[0] == xVal-1 and p[1] == yVal-1:
                if p[2] < minCount:
                    minCount = p[2]
        return minCount
    
grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
grid = [[0,2,4],[3,2,1],[1,0,4]]
answer = Solution.minimumTime(grid)
print(answer)