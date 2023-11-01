from copy  import deepcopy

class Solution:
    def beautifulPartitions(s, k, minLength):
        primeList = ["2", "3", "5", "7"]
        enumString = list(enumerate(s))
        partition = k
        print(s)
        print(enumString)
        endTurn = k
        dp = []
        if s[0] not in primeList and s[-1] in primeList:
            return 0
        partitionList = []
        prevList = []
        endList = []
        alternateK = False
        #Bottom up iterative approach to dynamic programming solution for this problem. (More harder to explain) 
        while(k!= 0):
            #Get first partition
            print("dp is: ", dp)
            if(k == endTurn):
                for c in range(minLength-1, len(s)-(k-1)*minLength):
                    if (s[c] not in primeList and s[c+1] in primeList):
                        partitionList.append((enumString[c][0], s[:enumString[c+1][0]]))
                print("Partition list is: ",partitionList)
                k-=1
                dp += partitionList
                prevList = list(deepcopy(partitionList))
                #print("dp is: ", dp)
                continue
            #Get last partitions
            if(k-1 == 0):
                print("End lists prevList is: ", prevList)
                for ind, string in prevList:
                    #print("index at endstring now is: ", ind)
                    for c in range(ind+minLength,len(s)):
                        if (enumString[c][1] not in primeList and enumString[ind+1][1] in primeList):
                            endList.append((enumString[c][0], s[ind+1:enumString[c][0]+1]))
                print("Endlist is: ", endList)
                k-=1
                dp += endList
                continue
            tempList = []
            for ind, string in prevList:
                print("current index it: ", ind)
                for c in range(ind+minLength,len(s)-(k-1)*minLength):

                    if (enumString[c][1] not in primeList and enumString[c+1][1] in primeList):
                        tempList.append((enumString[c][0], s[ind+1:enumString[c+1][0]]))

            prevList = list(deepcopy(tempList))
            print("Prev List is: ", prevList)
            k-=1
            dp += tempList
        count = 0
        print(dp)
        endInd = len(s)
        #Apparently this is not needed, what can be counted is the actual nodes that reached with index 10 and thats
        #The answer
        for i in dp:
            if i[0] == len(s)-1:
                count +=1
        #for i in dp:
        #    print("loop main dp", i)
        #    tempInd = i[0]
        #    tempPartition = partition
        #    successList = []
        #    while (tempPartition > 0):
        #        for j in dp:
        #            if(tempPartition == 0):
        #                break
        #            if j[0] < tempInd:
        #                continue
        #            print("Partition count and j value are: ",tempPartition, j)
        #            #print("loop while dp j", j)
        #            if tempPartition - 1 == 0 and tempInd == 10:
        #                count +=1
        #                successList.append(j)
        #                print("A successful List is: ", successList)
        #                successList = []
        #            tempPartition = tempPartition - 1
        #            successList.append(j)
        #            tempInd = j[0]

        return count


s = "3312958"
k = 3
minLength = 1
MODN = 10**9+7
answer = Solution.beautifulPartitions(s, k, minLength)
print(answer % MODN)