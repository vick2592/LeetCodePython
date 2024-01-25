import random
from functools import cache
from copy import deepcopy
import math

class Solution:
    dp = []
    
    #The solution is suppossed to be recurively splitting a string into two parts randomly until the string is of length 1 and then checking the merged output if it matches s2
    def isScramble(self, s1, s2):
        found = False
        def catalan(n):
            c = math.comb(2*n, n) // (n + 1)
            print("The catalan number and max combinations are: ", c, 2**c)
            return 2**c
        #@cache
        def recurseSplit(s):
            if len(s) == 1:
                return s
            else:
                randomNum = random.randint(1, len(s)-1)
                sLeft = s[:randomNum]
                sRight = s[randomNum:]
                randomChoise = random.randint(0, 1)
                if randomChoise == 0:
                    return [sLeft] + [sRight]
                else:
                    return [sRight] + [sLeft]

        queueS = []
        for j in range(0, len(s1)):
            s1Left = s1[:j]
            s1Right = s1[j:]
            test1 = s1Left + s1Right
            test2 = s1Right + s1Left
            if test1 not in self.dp:
                queueS.append(test1)
                self.dp.append(test1)
            if test2 not in self.dp:
                queueS.append(test2)
                self.dp.append(test2)
        print(self.dp)
        print(recurseSplit(s1))
        cn = catalan(len(s1)-1)
        count = 0
        while(found != True):
            #testS = deepcopy(s1)
            splitList = recurseSplit(s1)
            #print(splitList)
            while(len(splitList)) != len(s1):
                tempList = []
                for i in splitList:
                    tempList += recurseSplit(i)
                splitList = tempList
            newS = "".join(splitList)
            # print(newS)
            if newS not in self.dp:
                self.dp.append(newS)
            # print(splitList)
            if newS == s2:
                found = True
                #break
            if len(self.dp) == cn:
                break
            count += 1
            if count > cn:
                break
            print(count, cn)
        print(self.dp)
        return found
    
s1 = "great"
s2 = "rgeat"
# s1 = "abcde"
# s2 = "caebd"
answer = Solution()

print(answer.isScramble(s1, s2))
n = 4
print(math.comb(2*n, n) - math.comb(2*n, n-1))