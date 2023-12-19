class Solution:
    def largestDivisibleSubset(nums):
        nSet = []
        for i in range(len(nums)):
            tempT = [nums[i]]
            for j in range(i+1, len(nums)):
                tempT.append(nums[j])
                thisTuple = tuple(tempT)
                if thisTuple not in nSet:
                    nSet.append(thisTuple)
                    
        nSet = sorted(nSet, key=lambda x: len(x), reverse=True)
        for n in range(len(nSet)):
            print(nSet[n])
            ans = True
            for i in range(len(nSet[n])):
                for j in range(i+1, len(nSet[n])):
                    if nSet[n][i] % nSet[n][j] == 0 or nSet[n][j] % nSet[n][i] == 0:
                        continue
                    ans = False
                    break
            if ans:
                return list(nSet[n])

        print(nSet)
        return []
    

    
nums = [1,2,4,8]
answer = Solution.largestDivisibleSubset(nums)
print(answer)