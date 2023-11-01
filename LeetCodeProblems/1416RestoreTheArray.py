from copy import deepcopy

class Solution:
    def numberOfArrays(s, k):

        #Define helper function to get length. 
        def getTotalLen(strTups, length):
            answer = 0
            for i in range(length):
                answer += strTups[i][1]
            return answer

        #Initially create your most lowest integer values from string.
        strList = []
        for idx, c in list(enumerate(s)):
            if (c == '0'):
                continue
            tempStr = c
            if (idx+1 == len(s)):
                strList.append(s[idx])
                break
            for i in range(idx+1, len(s)):
                if s[i] == '0':
                    tempStr = tempStr + s[i]

                if s[i] != '0':
                    strList.append(tempStr)
                    break
        #Check if you need to exit case. 
        for num in strList:
            if(int(num)/k >= 1):
                return 0

        strTupList = []
        for n in strList:
            strTupList.append((str(n), len(str(n))))

        print(strTupList)
        allCombs = []
        data = []
        kSize = len(str(k))
        print("K size is: ", kSize)
        longestComb = ''
        longestcount = 0
        #base case plus max size comb closest to k size requirement and n number of acceptable integers.
        for i in range(len(strTupList)):
            oneNcomb = ''
            oneNcount = 0
            for j in range(i, len(strTupList)):
                if(oneNcount + strTupList[j][1] > kSize and oneNcount == 0):
                    break
                elif (oneNcount + strTupList[j][1] > kSize):
                    if ((i,len(oneNcomb), oneNcomb) not in data):
                        #Quick fix if the size of item on i index greater than one you must adjust index. 
                        data.append((i,len(oneNcomb),oneNcomb ))
                    print("Current elif part i, j, and oneNcomb is: ", i, j, oneNcomb)
                    if (longestComb == ''):
                        longestComb = oneNcomb
                        longestcount = oneNcount
                    elif (int(longestComb) < int(oneNcomb) and int(oneNcomb)/k < 1):
                        longestComb = oneNcomb
                        longestcount = oneNcount
                else:
                    oneNcomb += strTupList[j][0]
                    oneNcount += strTupList[j][1]
                    if ((i,len(oneNcomb), oneNcomb) not in data):
                        data.append((i,len(oneNcomb), oneNcomb))
                    print("Current else part of loop i, j, and oneNcomb is: ", i, j, oneNcomb)
                    if (longestComb == ''):
                        longestComb = oneNcomb
                        longestcount = oneNcount
                    elif (int(longestComb) < int(oneNcomb) and int(oneNcomb)/k < 1):
                        longestComb = oneNcomb
                        longestcount = oneNcount

        print("DATA: ", data)
        pq = []

        for cur in data:
            if (cur[0] == 0):
                startList = []
                startList.append(cur[2])
                pq.append((cur[0]+cur[1],startList))
        print("Starting pq is: ", pq)
        count = 0

        while (len(pq) != 0 and count < 50):
            checkQ = pq[0]
            qSize = checkQ[0]
            print("Initial CheckQ value amd qSize: ", checkQ, qSize)
            print()

            #Base case for if there is no cur since array allready qSize
            if(checkQ[0] == len(s)):
                allCombs.append(checkQ[1])
                print("Combination added to list: ", checkQ[1])
                pq.pop(0)
                count += 1
                print("Current step count is: ", count)
                print("-------------------------- ")
                continue

            for cur in data:
                tempPq = deepcopy(checkQ)
                tempQsize = qSize
                if (getTotalLen(strTupList, cur[0]) == qSize):
                    print("tempQ current is: ", tempPq)
                    print()

                    #Check if you found a full combination
                    if(tempQsize + cur[1] == len(s)):
                        tempPq[1].append(cur[2])
                        allCombs.append(tempPq[1])
                        print("Combination added to list: ", tempPq[1])
                        continue
                    tempPq[1].append(cur[2])
                    if(tempPq not in pq):
                        pq.append((tempQsize + cur[1], tempPq[1]))
                    print("Current priority queue: ", pq)

            print("We are about to pop front of pq")
            pq.pop(0)
            print("pq after removing front", pq)
            count += 1
            print("Current step count is: ", count)
            print("+++++++++++++++++++++++++")
        print("All Combinations at the end are: ",allCombs)

        return len(allCombs)

s = "13071908"
#s = "1317"
k = 2000

answer = Solution.numberOfArrays(s, k)
print(answer)


