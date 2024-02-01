from itertools import permutations, combinations

class Solution:
    def maxHeight(cuboids):
        ans = 0
        enumL = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,1,0], [2,0,1]]
        permL = list(permutations(range(len(cuboids)), len(cuboids)))
        #print(permL)
        # for p in permL:
        #     tempList = []
        #     for i in p:
        #         tempList.append(cuboids[i])
        #     for t in tempList:
        #         for e in enumL:
        sortL = []
        i = 0
        for c in cuboids:
            sortL.append([max(c), i])
            i += 1
        sortL = sorted(sortL, key=lambda x: x[0], reverse=True) 
        #print(sortL)
        newList = []
        for s in sortL:
            newList.append(cuboids[s[1]])
            
        ThreeDList = []
        for j in permL:
            tempL = []
            for k in j:
                tempL.append(newList[k])
            ThreeDList.append(tempL)
            
            
        #print(ThreeDList)     
        #print(newList)
        for e in range(len(ThreeDList)):
            #print("we are calcuating the sum from this e:" , ThreeDList[e])
            height = 0
            for a in range(1):
                for b in enumL:
                    testList1 = []
                    testList1.append(ThreeDList[e][a][b[0]])
                    testList1.append(ThreeDList[e][a][b[1]])
                    testList1.append(ThreeDList[e][a][b[2]])
                    #print(testList)
                    #tempHeight = testList1[2]
                    tempHeight = testList1[2]
                    for c in range(a+1, len(ThreeDList[e])):
                        prevHeight = 0
                        for d in enumL:
                            #print("temp height and prev height are: ", tempHeight, prevHeight)
                            testList2 = []
                            testList2.append(ThreeDList[e][c][d[0]])
                            testList2.append(ThreeDList[e][c][d[1]])
                            testList2.append(ThreeDList[e][c][d[2]])
                            if testList2[0] <= testList1[0] and testList2[1] <= testList1[1] and testList2[2] <= testList1[2]:
                                if prevHeight > testList2[2]:
                                    continue
                                tempHeight -= prevHeight
                                prevHeight = testList2[2]
                                tempHeight += testList2[2]
                            #print(d, testList2, testList1, prevHeight, tempHeight)
                        #tempHeight += prevHeight
                        #print("Level of c and tempheight: ", c, tempHeight)
                    if height < tempHeight:
                        height = tempHeight
            if ans < height:
                ans = height


        if ans == 0:
            return max(newList[0])
        return ans
    
cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
#cuboids = [[38,25,45],[76,35,3]]
#cuboids = [[50,45,20],[95,37,53],[45,23,12]]

answer = Solution.maxHeight(cuboids)
print(answer)

