from math import floor

class Solution:
    def addOperators(num, target):
        ansList = []
        actions = ["+", "-", "*"]
        ansLen = 2*len(num)-1

        #Create evaluation function
        def evaluateExp(expression):
            pairList = []
            for i in range(0, len(expression)-2, 2):
                #print("Steps correct?: ", i)
                if (expression[i+1] == '*'):
                    pairList.append((expression[i:i+3],i, i+2, 1, int((i+i+2)/2)))
                else:
                    pairList.append((expression[i:i+3],i, i+2, 0, int((i+i+2)/2)))

            pairList = sorted(pairList, key=lambda x: x[3], reverse = True)
            #print("Starting pairList: ", pairList)
            opList = [-111111 for x in range(len(expression))]
            #print("Current opList is: ", opList)
            #prevIndex = pairList[0][1]
            value = int(expression[pairList[0][1]])
            #print("The PrevIndex, value, and curOp is: ", prevIndex, value, curOp)
            for pair in pairList:
                #if the operation value has not been found yet. 
                if(opList[pair[4]] == -111111):
                    #Check left value
                    leftVal = int(expression[pair[1]])
                    leftChanged = False
                    rightChanged = False
                    rightVal = int(expression[pair[2]])
                    if(pair[4] - 2 > 0):
                        if(opList[pair[4]-2] != -111111):
                            leftVal = opList[pair[4]-2]
                            leftChanged = True
                    if(pair[4] + 2 < len(expression)):
                        if(opList[pair[4]+2] != -111111):
                            rightChanged = True
                            rightVal = opList[pair[4]+2]
                    if(pair[0][1] == '*'):
                        value = leftVal * rightVal
                        #print("leftVal * rightVal = value ", leftVal, rightVal, value)
                    if(pair[0][1] == '-'):
                        value = leftVal - rightVal
                        #print("leftVal - rightVal = value ", leftVal, rightVal, value)
                    if(pair[0][1] == '+'):
                        value = leftVal + rightVal
                        #print("leftVal + rightVal = value ", leftVal, rightVal, value)
                    opList[pair[4]] = value
                    if(leftChanged):
                        opList[pair[4]-2] = value
                    if(rightChanged):
                        opList[pair[4]+2] = value

                #print("Current Pair list, and value is now: ", pairList, value)
                #print("Current addedPairs is: ", addedPair)
                #print("End Op List is: ", opList)

            return value

        #REDO THE FOR LOOP AS IT IS NOT INDEXING CORRECTLY. MAYBE SEE THAT YOU CAN DO INDEX BY LEN OF STRING LIKE ABS STRLEN / 2 + 1
        #Test function
        #test = evaluateExp("1-2-3")
        #print("Test result after running evaluateExp is: ", test)
        pq = []

        #Start Case
        pq.append((num[0], int(num[0])))
        print("Initial PQ and ansLen is: ", pq, ansLen)
        count = 0
        while (len(pq) != 0):
            #print("While loop started with pqlen as: ", len(pq))
            n = 0
            testStr, testVal = pq[0]
            if(len(testStr) == ansLen and testVal == target):
                if testStr not in ansList:
                    ansList.append(testStr)
            for n in range(3):
                #print("Current Inner while loop n value is: ", n)
                if(actions[n] == "+" and len(testStr) <= ansLen-2):
                    #print("First one is the sum with n: ", n)
                    tempStr = testStr
                    tempNum = testVal + int(num[floor(len(tempStr)/2)+1])
                    tempStr = tempStr + "+" + str(num[floor(len(tempStr)/2)+1])
                    pq.append((tempStr, evaluateExp(tempStr)))
                if(actions[n] == "-" and len(testStr) <= ansLen-2):
                    tempStr = testStr
                    tempNum = testVal - int(num[floor(len(tempStr)/2)+1])
                    tempStr = tempStr + "-" + str(num[floor(len(tempStr)/2)+1])
                    pq.append((tempStr, evaluateExp(tempStr)))
                if(actions[n] == "*" and len(testStr) <= ansLen-2):
                    tempStr = testStr
                    tempNum = testVal * int(num[floor(len(tempStr)/2)+1])
                    tempStr = tempStr + "*" + str(num[floor(len(tempStr)/2)+1])
                    pq.append((tempStr, evaluateExp(tempStr)))
            print("PQ and count is: ", pq, count)
            pq.pop(0)
            count = count + 1
        #print(ansList)
        return ansList

num = "123"
target = 6
num = "232"
target = 8

answer = Solution.addOperators(num, target)
print(answer)
