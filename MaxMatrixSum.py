import math

class Solution:
    def maxMatrixSum(matrix):
        abs_total = neg = 0
        mi= math.inf
        for row in matrix:
            for num in row:
                abs_total += abs(num)
                if num < 0:
                    neg += 1
                mi = min(mi, abs(num))
        return abs_total if neg % 2 == 0 else abs_total - 2 * mi


matrix1 = [[1,2,3],[-1,-2,-3],[1,2,3]]
print(Solution.maxMatrixSum(matrix1))