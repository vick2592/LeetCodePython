import math

class Solution:
    def projectionArea(grid):
        hor = sum(map(max, grid))
        print(*grid)
        print(list(zip(*grid)))
        ver = sum(map(max, zip(*grid)))
        top = sum(v > 0 for row in grid for v in row)
        return ver + hor + top


Grd = [[1,2],[3,4]]

answer = Solution.projectionArea(Grd)

print(answer)