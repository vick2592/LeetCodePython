from itertools import permutations
from copy import deepcopy

class Solution:
    def distinctSequences(num):
        def findGCD(a,b):
            aDivisors = []
            bDivisors = []
            for n in range(1, a+1):
                if a % n == 0:
                    aDivisors.append(n)
            for n in range(1, b+1):
                if b % n == 0:
                    bDivisors.append(n)

            #print(aDivisors)
            #print(bDivisors)

            GCD = 0
            for n in aDivisors:
                for m in bDivisors:
                    if n == m:
                        if n > GCD:
                            GCD = n
                    continue
            return GCD
        #Test GCD
        #testA = 3
        #testB = 1
        #testGCD = findGCD(testA, testB)
        #print(testGCD)

        countRemoved = 0
        die = [1,2,3,4,5,6] * num
        print(die)
        allPermutations = list(permutations(die, num))
        copyPermutations = deepcopy(allPermutations)
        #print(allPermutations)
        #Check to see if any adjecant value is divisable by 1 only. 
        for idx, perm in list(enumerate(allPermutations)):
            for jdx, n in list(enumerate(perm)):
                if (jdx == 0):
                    if(findGCD(n, perm[jdx + 1]) != 1):
                        #print(perm[jdx+1])
                        copyPermutations.pop(idx-countRemoved)
                        countRemoved +=1
                        break
                if (jdx == n-1):
                    if(findGCD(n, perm[jdx - 1]) != 1):
                        copyPermutations.pop(idx-countRemoved)
                        countRemoved +=1
                        break
                if (jdx > 0 and jdx < num -1):
                    if(findGCD(n, perm[jdx - 1]) != 1 or findGCD(n, perm[jdx + 1]) != 1):
                        #print(jdx, perm[jdx])
                        copyPermutations.pop(idx-countRemoved)
                        countRemoved +=1
                        break

        #print(copyPermutations[:100])
        print(len(copyPermutations))
        copyGCDPermutations = deepcopy(copyPermutations)
        countIJremoved = 0
        for idx, perm in list(enumerate(copyPermutations)):
            for jdx, n in list(enumerate(perm)):
                if (jdx == 0):
                    #If start
                    if (n == perm[jdx + 1] or n == perm[jdx + 2]):
                        copyGCDPermutations.pop(idx-countIJremoved)
                        countIJremoved +=1
                        break
                if (jdx == n-1):
                    #If end
                    if (n == perm[jdx - 1] or n == perm[jdx - 2]):
                        copyGCDPermutations.pop(idx-countIJremoved)
                        countIJremoved +=1
                        break
                if (jdx > 0 and jdx < num -1):
                    #If -1, -2, +1 but not +2
                    if(jdx - 1 >= 0 and jdx - 2 < 0 and jdx + 1 <= num -1 and jdx + 2 > num -1): 
                        if (n == perm[jdx - 1] or n == perm[jdx - 2] or n == perm[jdx + 1]):
                            copyGCDPermutations.pop(idx-countIJremoved)
                            countIJremoved +=1
                            break
                    #If -1, -2, +1, +2
                    if(jdx - 1 >= 0 and jdx - 2 >= 0 and jdx + 1 <= num -1 and jdx + 2 <= num -1):
                        if (n == perm[jdx - 1] or n == perm[jdx - 2] or n == perm[jdx + 1] or n == perm[jdx + 2]):
                            copyGCDPermutations.pop(idx-countIJremoved)
                            countIJremoved +=1
                            break
                    #if -1 not -2, +1 and + 2
                    if(jdx - 1 >= 0 and jdx - 2 < 0 and jdx + 1 <= num -1 and jdx + 2 <= num -1): 
                        if (n == perm[jdx - 1] or n == perm[jdx + 1] or n == perm[jdx + 2]):
                            copyGCDPermutations.pop(idx-countIJremoved)
                            countIJremoved +=1
                            break
                    #if -1 not -2, +1 and not + 2
                    if(jdx - 1 >= 0 and jdx - 2 < 0 and jdx + 1 <= num -1 and jdx + 2 > num -1): 
                        if (n == perm[jdx - 1] or n == perm[jdx + 1]):
                            copyGCDPermutations.pop(idx-countIJremoved)
                            countIJremoved +=1
                            break
       
        print(copyGCDPermutations[:100])
        print(len(copyGCDPermutations))

        #Delete the duplicates
        MOD = 10**9+7
        answerList = []
        for perm in copyGCDPermutations:
            if perm not in answerList:
                answerList.append(perm)

        answer = len(answerList) % MOD
        return answer

n = 4

answer = Solution.distinctSequences(n)
print(answer)