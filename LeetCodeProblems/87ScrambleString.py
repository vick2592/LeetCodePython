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
            return math.comb(2*n, n) // (n + 1)
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
        while(found != True):
            #testS = deepcopy(s1)
            splitList = recurseSplit(s1)
            print(splitList)
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
            if len(self.dp) == catalan(len(s1)):
                break
        print(self.dp)
        return found
    
s1 = "great"
s2 = "rgeat"
# s1 = "abcde"
# s2 = "caebd"
answer = Solution()

print(answer.isScramble(s1, s2))


        # queueList = []
        # queueList.append(s1)
        # self.dp.append(s1)
        # while(len(queueList) > 0):
        #     s1 = queueList.pop(0)
        #     for x in range(0, len(s1)):
        #         s1Left = s1[:x]
        #         s1Right = s1[x:]
        #         test1 = s1Left + s1Right
        #         test2 = s1Right + s1Left
        #         print(test1, test2)
        #         if test1 not in self.dp:
        #             queueList.append(test1)
        #             self.dp.append(test1)
        #         if test2 not in self.dp:
        #             queueList.append(test2)
        #             self.dp.append(test2)
        # if (s1 not in self.dp):
        #     self.dp.append(s1)
        # else:
        #     return
        # if len(s1) == 1:
        #     if s1 == s2:
        #         return True
        #     else:
        #         return False
            
        # if len(s1) > 1:
        #     randomNum = random.randint(1, len(s1))
            
        # s1Left = s1[:randomNum]
        # s1Right = s1[randomNum:]
        # test1 = s1Left + s1Right
        # test2 = s1Right + s1Left
        # print(test1, test2)
        # self.isScramble(test1, s2) 
        #     # if test1 == s2:
        #     #     return True 

        # self.isScramble(test2, s2) 
        #     # if test2 == s2:
        #     #     return True 