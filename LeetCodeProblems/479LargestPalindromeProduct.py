class Solution:
    def largestPalindrome(n):
        def isPalindrome(nList):
            nSize = len(nList) - 1
            for x in range(nSize//2):
                if(nList[x] != nList[nSize - x]):
                    return False
            return True

        if n == 1:
            return 9

        largestN = ""
        tempN = n
        while(tempN > 0):
            largestN += "9"
            tempN -= 1

        largestIntN = int(largestN)
        nX = largestIntN
        nY = largestIntN
        palindromeFound = False
        palindromeN = -1
        while nX > 0:
            while nY > 0:
                testN = nX * nY
                testNstr = list(str(testN))
                if(isPalindrome(testNstr)):
                    return testN % 1337
                else:
                    nY -= 1

            nX -= 1
            nY = largestIntN


        if palindromeFound == False:
            return 0

        return palindromeN 

n = 2
answer = Solution.largestPalindrome(n)
print(answer)