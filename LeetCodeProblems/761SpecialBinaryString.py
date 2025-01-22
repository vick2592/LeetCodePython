class Solution:
    # def makeLargestSpecial(s):
    #     def helper(s):
    #         oneC = sum([1 for c in s if c == "1"])
    #         zeroC = sum([1 for c in s if c == "0"])
    #         if oneC != zeroC:
    #             return False
    #         if s[0] == "0":
    #             return False
    #         splitOne = list(filter(None, s.split("1")))
    #         splitZero = list(filter(None, s.split("0")))
    #         # print(splitOne, splitZero)
    #         if len(splitOne) != len(splitZero):
    #             return False
    #         for i in range(len(splitOne)):
    #             if len(splitOne[i]) != len(splitZero[i]):
    #                 return False
    #         return True
    #     # print(helper("1100"))
    #     # print(helper(s))
    #     subStrings = []
    #     for x in range(len(s)):
    #         for y in range(x+1, len(s)):
    #             if helper(s[x:y+1]) and s[x:y+1] not in subStrings:
    #                 subStrings.append((s[x:y+1], x))
    #     print(subStrings)

    #     subStrings.sort(key=lambda x: x[0], reverse=True)
    #     print(subStrings)
    #     #how to get max lexiographically largest string after some number of swaps of these strings
    #     # allStrings = []
    #     # for x in range(len(s)):
    #     #     pString = ""
    #     #     usedInd = []
    #     #     sInd = 0
    #     #     for y in range(x, len(s)):
    #     #         for j in range(len(subStrings)):
    #     #             if subStrings[j][1] not in usedInd:
    #     #                 pString += subStrings[j][0]
    #     #                 usedInd.append(subStrings[j][1])
    #     #                 sInd = len(pString)
    #     #         pString += s[y]


    #     #     allStrings.append(pString)
    #     # print(allStrings)

    #     result = []
    #     i = 0
    #     while i < len(s):
    #         if any(i == idx for _, idx in subStrings):
    #             for sub, idx in subStrings:
    #                 if i == idx:
    #                     result.append(sub)
    #                     i += len(sub)
    #                     break
    #         else:
    #             result.append(s[i])
    #             i += 1

    #     return ''.join(result)

    def makeLargestSpecial(s):
        count = i = 0
        res = []
        for j, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            if count == 0:
                res.append('1' + Solution.makeLargestSpecial(s[i + 1:j]) + '0')
                i = j + 1
        return ''.join(sorted(res, reverse=True))
s = "11011000"
answer = Solution.makeLargestSpecial(s)
print(answer)