import math

class Solution:
    def hammingDistance(x, y):
        dtb = Solution()

        binX = dtb.decitoBin(x)
        binY = dtb.decitoBin(y)

        binSizeX = len(binX)
        binSizeY = len(binY)
        binSizeDiff = abs(binSizeX - binSizeY)

        if (binSizeDiff != 0):
            if (binSizeX > binSizeY):
                binY = ('0' * binSizeDiff) + binY 
                #print("Updated BinY is: ", binY)
            if (binSizeY > binSizeX):
                binX = ('0' * binSizeDiff) + binX
                #print("Updated BinX is: ", binX)

        totalSize = len(binX)

        hammingCount = 0
        for i in range(0, totalSize):
            if (binX[i] != binY[i]):
                hammingCount += 1

        #print(binSizeY)
        #print(binY)

        return hammingCount

    def decitoBin(self, numb):
      # converting it to binary representation using bin() function
        binNumb = bin(numb)
        # replacing '0b' using replace function and replacing it with empty string
        binNumb = binNumb.replace('0b', '')
      # return the binary representation of the given number
        return binNumb

x = 1
y = 4

answer = Solution.hammingDistance(x,y)

print(answer)