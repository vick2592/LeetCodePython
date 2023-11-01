from copy import deepcopy

#Note this was a quick and dirty way to get to the solution but was not the most opitimal one.
#To fix you should add a queue and do a BFS method where you keep track of all cells x,y,c where x is row, y is column, and c is obstacles removed.
#Keep going adding all the visited elements and their related counts and then sort by c.
#From there your answer will be the corner with shortest c. 

class Solution:
    reachedEnd = False
    def minimumObstacles(grid):
        def helper(grid, x, y, dp):
            if(x == len(grid)-1 and y == len(grid[0])-1):
                Solution.reachedEnd = True
            print(x,y)
            dp[x][y] = 1
            if ((x+1) < len(grid) and dp[x+1][y] == 0 and grid[x+1][y] == 0):
                helper(grid, x+1, y, dp)
            if ((y+1) < len(grid[0]) and dp[x][y+1] == 0 and grid[x][y+1] == 0):
                helper(grid, x, y+1, dp)
            if ((x-1) >= 0 and dp[x-1][y] == 0 and grid[x-1][y] == 0):
                helper(grid, x-1, y, dp)
            if ((y-1) >= 0 and dp[x][y-1] == 0 and grid[x][y-1] == 0):
                helper(grid, x, y-1, dp)

        count = 0
        dp = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        helper(grid, 0, 0, dp)
        tempGrid = deepcopy(grid)
        while (Solution.reachedEnd != True):
            nodeChanged = False
            for x in range(len(tempGrid)):
                if nodeChanged == True:
                    break
                for y in range(len(tempGrid[0])):
                    if (tempGrid[x][y] == 1):
                        tempGrid[x][y] = 0
                        nodeChanged = True
                        break
                        
            tempDP = [[0 for colY in range(len(grid[0]))] for rowX in range(len(grid))]
            helper(tempGrid, 0, 0, tempDP)
            count += 1

        return count

grid = [[0,1,1],[1,1,0],[1,1,0]]
# grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]

answer = Solution.minimumObstacles(grid)
print(answer)