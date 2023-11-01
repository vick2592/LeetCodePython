from copy import deepcopy
class Solution:
    def makeStringSorted(s):
        largeNum = 10^9+7
        answer = 0
        copyS = deepcopy(s)
        #Build a method to check if sorted at each step of recursion. 
        def sortedS(sNew):
            for c in range(len(sNew)):
                if c == len(sNew) - 1:
                    return True
                if ord(sNew[c]) > ord(sNew[c+1]):
                    break
            return False

        while(True):
            
            #scan for i to put in list
            iLst = []
            jLst = []
            for i in range(1, len(copyS)):
                if(copyS[i] < copyS[i-1] and i not in iLst):
                    iLst.append(i)
                #scan for j to put in List
                for j in range(i, len(copyS)):
                    if(copyS[j] < copyS[i-1] and j not in jLst):
                        jLst.append(j)

            iLst = sorted(iLst, reverse = True)
            jLst = sorted(jLst, reverse = True)
                
            print(iLst, jLst)
            iVal = 0
            jVal = 0
            foundIJ = False
            for i in iLst:
                for j in jLst:
                    if(copyS[j] < copyS[i-1]):
                        iVal = i
                        jVal = j
                        foundIJ = True
                        break
                if(foundIJ):
                    break 
            
            tempS = list(copyS)
            print("tempS is: ", tempS)
            tempS[jVal] = copyS[iVal - 1]
            tempS[iVal - 1] = copyS[jVal]
            #Testing the reverse will be in the second recusrive operation
            newStr = "".join(tempS[:iVal]) + "".join(reversed(tempS[iVal:]))

            print("newStr is: ", newStr)
            answer += 1
            #At this point keep recusring until string is sorted. 
            if (sortedS(newStr)):
                return answer % largeNum
            copyS = deepcopy(newStr)

        #At each step you can select an applicable i and j to do an operation. Recurse until you find shortest path and return that for each possible i, j pair.
        #You can do this by making seperate Class functions one to getPath which will run each of the steps and then check if sorted.
        #if sorted can be another class helper function that checks if string is sorted or not. Ofcourse if it is then recursive helper function would return the 
        #level of recursion by storing it into a varibale. This class variable (Argument) can act as a place holder for shortest path starting from largeNum.
        return answer % largeNum
s = "cba"
answer = Solution.makeStringSorted(s)
print(answer)


#Key steps are
    #Find the largest index i such that 1 <= i < s.length and s[i] < s[i - 1].
    #Find the largest index j such that i <= j < s.length and s[k] < s[i - 1] for all the possible values of k in the range [i, j] inclusive.
    #Swap the two characters at indices i - 1 and j.
    #Reverse the suffix starting at index i.
