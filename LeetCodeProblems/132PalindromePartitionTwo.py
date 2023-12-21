from copy import deepcopy

class Solution:
    def minCut(self, s):
        if i > len(s):
            return 
        def checkPalindrome(s):
            if len(s) == 1:
                return True
            for i in range(len(s)):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True
        if checkPalindrome(s) and len(cr) == 0:
            return 0
        allPossibilities = []
        for x in range(len(s)):
            for y in range(x, len(s)):
                allPossibilities.append((s[x:y+1],x,len(s[x:y+1])))
        #print(allPossibilities)
        matchPairs = []
        for x in range(len(allPossibilities)):
            if allPossibilities[x][1] == 0:   
                temp = [allPossibilities[x][0]]
                curInd = allPossibilities[x][1] + allPossibilities[x][2]
                clonedList = deepcopy(allPossibilities)
                clonedList.pop(x)
                while (len(clonedList) > 0):
                    addedList = []
                    for itm in clonedList:
                         if(itm[1] == allPossibilities[x][1]):
                            clonedList.pop(clonedList.index(itm))
                    for y in range(len(clonedList)):
                        if clonedList[y][1] == curInd and clonedList[y][2] + curInd <= len(s):
                           temp.append(clonedList[y][0])
                           curInd += clonedList[y][2]
                           addedList.append(clonedList[y])
                           # print(temp)
                        if curInd == len(s):
                           matchPairs.append(temp)
                           break
                    popInd = 0 
                    # print(addedList, "Added list is")
                    if len(addedList) == 0:
                        del clonedList[:]
                    for z in addedList: 
                        itmInd = clonedList.index(z)
                        clonedList.pop(itmInd)
                        #print(z)
                    temp = [allPossibilities[x][0]]
                    curInd = allPossibilities[x][1] + allPossibilities[x][2]
                    #print("current cloned List is: ", clonedList)
                    
        matchPairs = sorted(matchPairs, key=lambda x: len(x), reverse=False)
        print(matchPairs)
        for pr in matchPairs:
            matchFound = True
            for pd in pr:
                if checkPalindrome(pd) == False:
                    matchFound = False
                    break
            if matchFound:
                print("found match: ", pr)
                return len(pr)-1
                
        return 0
    
s = "aab"
answer = Solution()
#answer.minCut(s)
print(answer.minCut(s))

        
