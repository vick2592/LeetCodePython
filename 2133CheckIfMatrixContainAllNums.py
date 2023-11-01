class Solution:
    def checkValid(matrix):
 
        xSize = len(matrix)
        ySize = len(matrix[0])

        #Check each rows are fixed
        for x in range(1,xSize+1):
            #testList = [x for x in range(xSize)]
            #print(testList)
            for y in matrix:
                if x not in y:
                    return False
        #Get column List
        colList =  []
        for y in range(ySize):
            tempList = []
            for x in range(xSize):
                tempList.append(matrix[x][y])
            colList.append(tempList)

        #print(colList)
        for x in range(1,xSize+1):
            #testList = [x for x in range(xSize)]
            #print(testList)
            for y in colList:
                if x not in y:
                    return False

        return True

matrix = [[1,2,3],[3,1,2],[2,3,1]]
answer = Solution.checkValid(matrix)
print(answer)
