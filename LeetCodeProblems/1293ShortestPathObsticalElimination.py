from copy import deepcopy

class Solution:
    def shortestPath(grid, k):
        def shortestPathCount(grid):
            visited = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
            #print(visited)
            queue = [[0, 0, 0]]
            while queue:
                x, y, steps = queue.pop(0)
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return steps
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                        if grid[nx][ny] == 0 and visited[nx][ny] != 1:
                            visited[nx][ny] = 1
                            queue.append([nx, ny, steps + 1])
            return -1
        #print(shortestPathCount(grid))
        collection = []
        def recursiveInsert(grid, k):
            if k >= 0:
                collection.append(deepcopy(grid))  # Append a copy of the current grid configuration
            else:
                return  # Stop recursion if k < 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and k > 0:
                        temp = deepcopy(grid)
                        temp[i][j] = 0  # Remove obstacle
                        recursiveInsert(temp, k - 1) 

        recursiveInsert(grid,k)
        print(collection)
        
        smallest = 10**9+7
        for i in range(len(collection)):
            smallest = min(smallest, shortestPathCount(collection[i]))
        return smallest
    
grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1

answer = Solution.shortestPath(grid, k)
print(answer)  # Expected output: 6