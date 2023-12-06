class Solution:
    def islandPerimeter(grid):
        count = 0
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[x][y] == 1:
                    if x - 1 < 0 or grid[x-1][y] == 0:
                        count += 1
                    if x + 1 >= len(grid[0]) or grid[x+1][y] == 0:
                        count += 1
                    if y - 1 < 0 or grid[x][y-1] == 0:
                        count += 1
                    if y + 1 >= len(grid) or grid[x][y+1] == 0:
                        count += 1
                        
                    
        return count
    
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

answer = Solution.islandPerimeter(grid)
print(answer)