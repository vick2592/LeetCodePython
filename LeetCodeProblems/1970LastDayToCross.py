class Solution:
    def latestDayToCross(row, col, cells):
        ans = 0
        matrix = [[0 for i in range(col)] for j in range(row)]
        for i in range(len(cells)):
            matrix[cells[i][0]-1][cells[i][1]-1] = 1
            print(matrix)
            currentMoves = []
            queueMoves = []
            for j in range(col):
                if matrix[0][j] == 0:
                    queueMoves.append([0,j])
                    currentMoves.append([0,j])
            while (len(queueMoves) > 0):
                testNode = queueMoves.pop(0)
                if testNode[0] == row-1:
                    ans += 1
                    print("The current path is:" , currentMoves)
                    break
                else:
                    if testNode[0] + 1 < row and matrix[testNode[0]+1][testNode[1]] == 0 and [testNode[0]+1, testNode[1]] not in currentMoves:
                        queueMoves.append([testNode[0]+1, testNode[1]])
                        currentMoves.append([testNode[0]+1, testNode[1]])
                    if testNode[0] - 1 >= 0 and matrix[testNode[0]-1][testNode[1]] == 0 and [testNode[0]-1, testNode[1]] not in currentMoves:
                        queueMoves.append([testNode[0]-1, testNode[1]])
                        currentMoves.append([testNode[0]-1, testNode[1]])
                    if testNode[1] + 1 < col and matrix[testNode[0]][testNode[1]+1] == 0 and [testNode[0], testNode[1]+1] not in currentMoves:
                        queueMoves.append([testNode[0], testNode[1]+1])
                        currentMoves.append([testNode[0], testNode[1]+1])
                    if testNode[1] - 1 >= 0 and matrix[testNode[0]][testNode[1]-1] == 0 and [testNode[0], testNode[1]-1] not in currentMoves:
                        queueMoves.append([testNode[0], testNode[1]-1])
                        currentMoves.append([testNode[0], testNode[1]-1])
                
            
        return ans
    
row = 3
col = 3
cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]

row = 2
col = 2
cells = [[1,1],[2,1],[1,2],[2,2]]

row = 2
col = 2
cells = [[1,1],[1,2],[2,1],[2,2]]

answer = Solution.latestDayToCross(row, col, cells)
print(answer)