class Solution:
    def minimumVisitedCells(grid):
        queueL = []
        x = len(grid)
        y = len(grid[0])
        queueL.append([0, 0, 1])
        visited = set()
        minCount = 10** 9+7
        while (len(queueL) > 0):
            cur = queueL.pop(0)
            print(cur)
            if cur[0] >= x or cur[1] >= y or cur[0] < 0 or cur[1] < 0 or (cur[0], cur[1]) in visited:
                continue
            visited.add((cur[0], cur[1]))
            if cur[0] == x - 1 and cur[1] == y - 1:
                minCount = min(minCount, cur[2])
            for i in range(cur[1] + 1, min(y, cur[1] + grid[cur[0]][cur[1]] + 1)):
                queueL.append([cur[0], i, cur[2] + 1])
            for i in range(cur[0] + 1, min(x, cur[0] + grid[cur[0]][cur[1]] + 1)):
                queueL.append([i, cur[1], cur[2] + 1])
        if minCount != 10**9+7:
            return minCount
        return -1
        
grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
print(Solution.minimumVisitedCells(grid)) #0