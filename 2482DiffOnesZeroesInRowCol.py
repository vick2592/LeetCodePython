class Solution:
    def onesMinusZeros(grid):
        diff = [[0]*len(grid) for c in range(len(grid))]
        #print(newGrid)
        #For each value get the calculation and record
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                TempOnesCountRow = 0
                TempOnesCountCol = 0
                TempZeroesCountRow = 0
                TempZeroesCountCol = 0
                for tempX in range(len(grid)):
                    if(grid[tempX][y] == 0):
                        TempZeroesCountRow += 1
                        continue;
                    TempOnesCountRow += 1
                for tempY in range(len(grid[0])):
                    if(grid[x][tempY] == 0):
                        TempZeroesCountCol += 1
                        continue
                    TempOnesCountCol += 1
                diff[x][y] = TempOnesCountCol + TempOnesCountRow - TempZeroesCountRow - TempZeroesCountCol

        return diff
grid = [[0,1,1],[1,0,1],[0,0,1]]
#Return a grid that is modified with the differences of ones and zeroes Row and Col. 
answer = Solution.onesMinusZeros(grid)
print(answer)

    #Let the number of ones in the ith row be onesRowi.
    #Let the number of ones in the jth column be onesColj.
    #Let the number of zeros in the ith row be zerosRowi.
    #Let the number of zeros in the jth column be zerosColj.
    #diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
