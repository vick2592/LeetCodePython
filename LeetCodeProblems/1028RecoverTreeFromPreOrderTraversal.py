class Solution:
    def recoverFromPreorder(traversal):
        matrixMap = {}
        dashCount = 0
        prevCount = 0
        tempList = []
        numStr = ""
        for c in range(0, len(traversal)):
            if traversal[c]!="-":
                numStr += traversal[c]
                if (c == len(traversal) - 1):
                    matrixMap[numStr] = dashCount
                    tempList.append((numStr, dashCount))
                    dashCount = 0
                    numStr = ""
                continue
            if len(numStr) > 0:
                matrixMap[numStr] = dashCount
                tempList.append((numStr, dashCount))
                dashCount = 0
                numStr = ""
            dashCount +=1

        #sortMap = dict(sorted(matrixMap.items(), key=lambda item: item[1]))
        #print(list(matrixMap.items()))
        print("The templist is: ", tempList)
        #maxLevel = 0
        #for j in tempList:
        #    if (maxLevel < j[1]):
        #        maxLevel = j[1]
        #print("Max level is: ", maxLevel)
        
        #Preset a list of binary values by index.
        
        #matrixSize = 0
        #while(maxLevel >= 0):
        #    matrixSize += 2 ** maxLevel
        #    maxLevel -= 1
        #print("Matrix size is: ", matrixSize)
        #binList = []
        #for k in range(matrixSize):
        #    binList.append('null')

        #print(binList)
        #Add nulls
        #for tup in tempList:
        #    #print(tup[0], tup[1])
        #    binList[tup[1]*2+1] = tup[0]
        #level = 0
        #for ind, tup in list(enumerate(tempList)):
        #    if (ind == len(tempList) - 1):
        #        break
        #    curLev = tup[1]
        #    if(curLev == 0):
        #        binList[0] = tup[0]
        #        continue
        #    binList[level * 2 + 1] = tup[0]
        #    for i in range(ind+1, len(tempList)):
        #        if (tempList[i][1] == curLev):
        #            binList[level * 2 + 2] = tempList[i][0]
        #    level += 1
        #print(binList)

        #Check the sorted with the unsorted.
        #nullList = []
        #level = 0
        #for ind, tup in list(enumerate(tempList)):
        #    level = tup[1]
        #    binCount = level 
        #    nullList.append(tup)
        #    #print("Current level, index and tup is: ", level, ind, tup)
        #    prevLev = 0
        #    for i in range(ind+1, len(tempList)):
        #        if(tempList[i][1]==level):
        #            binCount -= 1
        #        if (prevLev < tempList[i][1]):
        #            prevLev = tempList[i][1]
        #            continue
        #        break

        #    if(binCount > 0):
        #        nullList.append("null")
        #print("The Null list is: ", nullList)
        matrixMap = sorted(matrixMap.items(), key=lambda item: item[1])
        print("Matrix Map is: ", matrixMap)

        test = []
        halfBin = False
        splitCount = 0
        for n in matrixMap:
            if n[1] == 1:
                splitCount += 1
        if(splitCount < 2):
            halfBin = True
        for p in matrixMap:
            lev = p[1]
            count = 2 ** lev - 1
            test.append(p[0])
            for m in tempList:
                if(m == p):
                    continue
                if(m[1] == lev):
                    count -= 1
                if(count == 0):
                    break
            if(halfBin):
                if count % 2 - 1== 0:
                    test.append('null')
                continue
            if (count > 0):
                test.append('null')

        print("The test set is: ", test)
        return test
        #output = []
        #for k, v in matrixMap:
        #    output.append(k)
        #return output

traversal = "1-2--3--4-5--6--7"
traversal = "1-2--3---4-5--6---7"
#traversal = "1-401--349---90--88"

answer = Solution.recoverFromPreorder(traversal)

print(answer)