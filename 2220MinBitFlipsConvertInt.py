import math

class Solution:
    def minBitFlips(start, goal):

        dtb = Solution()

        startBin = dtb.decitoBin(start)
        goalBin = dtb.decitoBin(goal)

        startZeroCount = 0
        startOneCount = 0

        goalZeroCount = 0 
        goalOneCount = 0

        for i in startBin:
            if(int(i) == 0):
                startZeroCount += 1
            elif(int(i) == 1):
                startOneCount += 1
            else:
                continue

        for i in goalBin:
            if(int(i) == 0):
                goalZeroCount += 1
            elif(int(i) == 1):
                goalOneCount += 1
            else:
                continue

        print(startZeroCount, "s0 ", startOneCount, " s1 ", goalZeroCount, " g0 ", goalOneCount, " g1", )
        return (abs(startZeroCount - goalZeroCount))+(abs(startOneCount - goalOneCount))

    def decitoBin(self, numb):
      # converting it to binary representation using bin() function
        binNumb = bin(numb)
        # replacing '0b' using replace function and replacing it with empty string
        binNumb = binNumb.replace('0b', '')
      # return the binary representation of the given number
        return binNumb



start = 10
goal = 7

# To get the answer compare and contrast each binary value and then count then umbers that are different in each index. Count is the answer
answer = Solution.minBitFlips(start,goal)
print(answer)