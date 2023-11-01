class Solution:
    def countDigitOne(n):
        countOne = 0
        for num in range(1,n+1):
            numStr = str(num)
            for c in numStr:
                if(c == "1"):
                    countOne += 1

        return countOne
n = 13
answer = Solution.countDigitOne(n)
print(answer)