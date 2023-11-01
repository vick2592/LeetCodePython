class Solution:
    def countBattleships(board):
        shipCount = 0
        rowSize = len(board)
        colSize = len(board[0]) 
        usedIndexes = []
        vertical = False
        horizontal = False
        #Scan horizontally the matrix. 
        for x in range(rowSize):
            for y in range(colSize):
                if(board[x][y] == 'X'):
                    if ((x,y) in usedIndexes):
                        continue
                    usedIndexes.append((x,y))
                    print("Current board value is: ", board[x][y])
                    print("Current usedIndexes is: ", usedIndexes)
                    #Check if Horizontal
                    for col in range(y, colSize):
                        print("Current horizontal check x and col: ", x, col)
                        if ((x,col) in usedIndexes):
                            continue
                        if (board[x][col] == 'X'):
                            horizontal = True
                            usedIndexes.append((x,col))
                            continue
                        if (board[x][col] == '.'):
                            break
                    if horizontal == True:
                        shipCount += 1
                        print("Current ship Count Horizontal: ", shipCount)
                        horizontal == False
                        continue
                    #Check if vertical
                    for row in range(x, rowSize):
                        print("Current vertical check x and col: ", row, y)
                        if ((row,y) in usedIndexes):
                            print("row and y are in usedIndexes: ", row, y)
                            continue
                        if (board[row][y] == 'X'):
                            vertical = True
                            usedIndexes.append((row,y))
                            continue
                        if (board[x][col] == '.'):
                            break
                    if vertical == True:
                        shipCount += 1
                        print("Current ship Count Vertical: ", shipCount)
                        vertical == False
                        continue
                    shipCount += 1
                    print("Current ship Count Niether: ", shipCount)
        print(usedIndexes)
        return shipCount

board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
answer = Solution.countBattleships(board)

print(answer)