class Solution:
    def nearestExit(maze, entrance):
        queue = []
        queue.append(entrance)
        visited = {}
        visited[tuple(entrance)] = 0
        endRow = len(maze)-1
        endCol = len(maze[0])-1
        step = 0
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur[0] - 1 >= 0:
                if maze[cur[0]-1][cur[1]] == "." and [cur[0]-1, cur[1]] not in list(visited.keys()):
                    queue.append([cur[0]-1, cur[1]])
                    visited[(cur[0]-1, cur[1])] = step + 1
                    if cur[0]-1 == 0 or cur[0]-1 == endRow or cur[1] == 0 or cur[1] == endCol:
                        return visited[(cur[0]-1, cur[1])]
            if cur[0] + 1 <= endRow:
                if maze[cur[0]+1][cur[1]] == "." and [cur[0]+1, cur[1]] not in list(visited.keys()):
                    queue.append([cur[0]+1, cur[1]])
                    visited[(cur[0]+1, cur[1])] = step + 1
                    if cur[0]+1 == 0 or cur[0]+1 == endRow or cur[1] == 0 or cur[1] == endCol:
                        return visited[(cur[0]+1, cur[1])]
            if cur[1] - 1 >= 0:
                if maze[cur[0]][cur[1]-1] == "." and [cur[0], cur[1]-1] not in list(visited.keys()):
                    queue.append([cur[0], cur[1]-1])
                    visited[(cur[0], cur[1]-1)] = step + 1
                    if cur[0] == 0 or cur[0] == endRow or cur[1]-1 == 0 or cur[1]-1 == endCol:
                        return visited[(cur[0], cur[1]-1)]
            if cur[1] + 1 <= endCol:
                if maze[cur[0]][cur[1]+1] == "." and [cur[0], cur[1]+1] not in list(visited.keys()):
                    queue.append([cur[0], cur[1]+1])
                    visited[(cur[0], cur[1]+1)] = step + 1
                    if cur[0] == 0 or cur[0] == endRow or cur[1]+1 == 0 or cur[1]+1 == endCol:
                        return visited[(cur[0], cur[1]+1)]
            step += 1
        
        return -1;


maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]
maze = [[".","+"]]
entrance = [0,0]

answer = Solution.nearestExit(maze, entrance)
print(answer)