class Solution:
    def maximumANDSum(nums, numSlots):
        selectedInd = []
        selectedNums = []
        numDict = {}
        for x in range(1, numSlots + 1):
            numDict[x] = []
        keyList = sorted(numDict.keys(), reverse = True)
        print(keyList)
        tempNums = sorted(nums, reverse= True)
        tempKeys = sorted(keyList, reverse= True)
        print("These are the temps: ",tempNums, tempKeys)
        for idx, num in enumerate(nums):
            notInSlot = False
            if num > keyList[0]:
                for k in keyList:
                    print("len of k is: ",k, len(numDict[k]))
                    if len(numDict[k]) < 2:
                        print("current len of key: ", len(numDict[k]))
                        if num & k > 0:
                            numDict[k].append(num)
                            selectedInd.append(idx)
                            notInSlot = True
                            break
                        else: 
                            continue
            if notInSlot or num not in keyList:
                continue
            if len(numDict[num]) < 2:
                numDict[num].append(num)
                selectedInd.append(idx)
                
        if len(selectedInd) != len(nums):
            for idx, num in enumerate(nums):
                if idx not in selectedInd:
                    for k in tempKeys:
                        if len(numDict[k]) < 2:
                            if num % k == 0:
                                numDict[k].append(num)
                                selectedInd.append(idx)
                                break
                            else:
                                continue
                        
        answer = 0
        for k,v in numDict.items():
            if len(v) != 0:
                for y in range(len(v)):
                    answer += k & v[y]
        print(numDict)
        return answer
            
                    
nums = [1,3,10,4,7,1]
numSlots = 9

# nums = [1,2,3,4,5,6]
# numSlots = 3

answer = Solution.maximumANDSum(nums, numSlots)

print(answer)