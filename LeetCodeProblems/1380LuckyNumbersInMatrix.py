class Solution:
    def luckyNumbers (matrix):
        luckyList = []
        rowSize = len(matrix[0])
        colSize = len(matrix)
        #print(rowSize,colSize)
        for i in range(colSize):
            for j in range(rowSize):
                test = matrix[i][j]
                minimum = False
                maximum = False
                #Check all Rows for minimum
                for k in range(rowSize):
                    if(j == k):
                        continue
                    if(test < matrix[i][k]):
                        minimum = True
                        continue
                    else:
                        minimum = False
                        break
                #Check all columns for Maximum
                for l in range(colSize):
                    if(i == l):
                        continue
                    if(test > matrix[l][j]):
                        maximum = True
                        continue
                    else:
                        maximum = False
                        break
                if(maximum == True and minimum == True):
                    luckyList.append(test)

        return luckyList

matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
answer = Solution.luckyNumbers(matrix)
print(answer)