from itertools import permutations, combinations
from copy import deepcopy
from math import floor


class Solution:
    count = 0
    def numSubmat(mat):
        def countMat(row, col, mat):
            print("Current row and col values are: ", row, col)
            countOnes = 0
            rowSize = len(mat)
            colSize = len(mat[0])
            matOnes = False
            for x in range(rowSize):
                for y in range(colSize):
                    if(x+row > rowSize):
                        return countOnes
                    if(y+col > colSize):
                        continue
                    for xRow in range(row):
                        for yCol in range(col):
                            print(x, y,xRow, yCol)
                            if(mat[xRow+x][yCol+y] == 1):
                                #print(x, y,xRow, yCol)
                                matOnes = True
                                continue
                            matOnes = False
                            break
                        if matOnes == False:
                            break
                    if matOnes == True:    
                        countOnes += 1
                        print("Count Ones is: ", countOnes)
                    matOnes == False

            return countOnes
        for x in range(len(mat)):
            for y in range(len(mat[0])):

                Solution.count = Solution.count + countMat(x+1, y+1, mat)
                print("Current count is: ", Solution.count)
                print("-----------------------")
        #    countMat(row, col+1, mat)
        
        #Getting the idex of each 2D array. 
        #enumMat = []
        #for i in range(len(mat[0])):
        #    enumMat.append(list(enumerate(mat[i])))
        #enumEnumMat = list(enumerate(enumMat))
        #print(enumEnumMat)
        #print("This is a same object")
        #print(list(enumMat))
        #combList = list(combinations(enumEnumMat[1], 2**9))
        #print(combList)
       # combMatrix = combinations(mat, 3)
        #print(list(combMatrix))

        return Solution.count


mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
answer = Solution.numSubmat(mat)
print(answer)