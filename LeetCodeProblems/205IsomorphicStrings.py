class Solution:
    def isIsomorphic(s, t):
        keyMapS = {}
        keyMapT = {}
        valMapS = {}
        valMapT = {}
        tEnum = list(enumerate(t))
        sEnum = list(enumerate(s))
        print(sEnum)
        for i in range(len(sEnum)):
            if sEnum[i][1] in keyMapS:
                keyMapS[sEnum[i][1]].append(sEnum[i][0])
            else:
                keyMapS[sEnum[i][1]] = [sEnum[i][0]]
        for i in range(len(tEnum)):
            if tEnum[i][1] in keyMapT:
                keyMapT[tEnum[i][1]].append(tEnum[i][0])
            else:
                keyMapT[tEnum[i][1]] = [tEnum[i][0]]

        for j in range(len(t)):
            if t[j] in valMapT:
                valMapT[t[j]] += 1
            else:
                valMapT[t[j]] = 1

        for j in range(len(s)):
            if s[j] in valMapS:
                valMapS[s[j]] += 1
            else:
                valMapS[s[j]] = 1


        print(keyMapS, valMapS)
        print(keyMapT, valMapT)
        for l in range(len(s)):
            if keyMapS[s[l]] != keyMapT[t[l]] and valMapS[s[l]] != valMapT[t[l]]:
                return False
                
        return True



s = "paper"
t = "title"
answer = Solution.isIsomorphic(s, t)
print(answer)  # Expected output: True