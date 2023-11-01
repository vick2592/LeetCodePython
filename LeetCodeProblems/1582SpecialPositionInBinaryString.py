class Solution:
    def numSpecial(mat):
        count = 0
        iSize = len(mat)
        jSize = len(mat[0])

        for i in range(0,iSize):
            for j in range(0, jSize):
                if (mat[i][j] == 1):
                    row = i
                    column = j
                    oneCountRow = 0
                    oneCountCol = 0
                    #Check Rows
                    for k in range(0, jSize):
                        if(mat[row][k] == 1):
                            oneCountRow += 1
                    #Check Columns 
                    for j in range(0, iSize):
                        if(mat[j][column] == 1):
                            oneCountCol += 1

                    if(oneCountRow == 1 and oneCountCol == 1):
                        count += 1



        return count

mat = [[1,0,0],[0,0,1],[1,0,0]]

answer = Solution.numSpecial(mat)

print(answer)

