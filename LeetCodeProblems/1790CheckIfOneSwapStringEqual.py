class Solution:
    def areAlmostEqual(s1, s2):
        for x in range(len(s1)):
            for y in range(len(s1)):
                if x == y:
                    continue
                tempS = [s for s in s1]
                #print("TempS is: ", tempS)
                tempC = tempS[x]
                tempS[x] = s1[y]
                tempS[y] = tempC
                newS = ''.join(tempS)
                if(newS == s2):
                    return True
        return False

s1 = "bank"
s2 = "kanb"
s1 = "attack"
s2 = "defend"

tempS = [s for s in s1]
print("TempS is: ", tempS)

answer = Solution.areAlmostEqual(s1,s2)
print(answer)