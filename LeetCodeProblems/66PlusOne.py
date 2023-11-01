class Solution:
    def plusOne(digits):
        numString = ""
        for i in digits:
            numString += str(i)

        print(numString)
        num = int(numString)
        num += 1
        stringNum = str(num)
        newList = []
        for j in stringNum:
            newList.append(int(j))

        return newList

digits = [4,3,2,1]

answer = Solution.plusOne(digits)
print(answer)