class Solution:
    def isFascinating(n):
        strN = str(n)
        strN2 = str(n * 2)
        strN3 = str(n * 3)
        strNAll = strN + strN2 + strN3
        test = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for c in strNAll:
            if c in test:
                test.remove(c)
                continue
            else:
                return False

        if len(test) == 0:
            return True
        else:
            return False

n = 192
n=100
answer = Solution.isFascinating(n)
print(answer)  # Expected output: True