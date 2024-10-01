class Solution:
    def titleToNumber(columnTitle):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabetDict = {}
        for i in range(len(alphabet)):
            alphabetDict[alphabet[i]] = i + 1
        columnNumber = 0
        for j in range(len(columnTitle)):
            columnNumber += alphabetDict[columnTitle[j]] * (26 ** (len(columnTitle) - j - 1))
        return columnNumber

columnTitle = "ZY"

answer = Solution.titleToNumber(columnTitle)
print(answer)