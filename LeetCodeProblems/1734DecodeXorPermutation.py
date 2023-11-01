class Solution:
    def decode(encoded): 
        n = len(encoded) + 1
        perm = [num for num in range(1,n+1)]
        for i in range(1, n+1):
            tempList = []
            tempList.append(i)
            temp = i
            for j in encoded:
                NotXorVal = temp^j
                tempList.append(NotXorVal)
                temp = NotXorVal
            tempDict = {}
            #print(tempList)
            for l in tempList:
                tempDict[l] = 0
            for k in tempList:
                if (k in perm):
                    tempDict[k] += 1
            decoded = False
            #print(tempDict)
            for k,v in tempDict.items():
                #print(k,v)
                if (k in perm and v == 1):
                    decoded = True
                    continue
                decoded = False
                break
            if(decoded == True):
                return tempList

            continue
                

encoded = [6,5,4,6]

answer = Solution.decode(encoded)
print(answer)