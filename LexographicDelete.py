from copy import copy

class Solution:
    def minDeletionSize(A):
        #print([True] * len(A))
        #for i in range(2):
        #    print(i)
        m, n, needToJudge, res = len(A), len(A[0]), [True] * len(A), 0
        for j in range(n):
            tep, flag = needToJudge[:], True
            print("iteration of letter j " + str(j) + " current need to Judge tep array " + str(tep))
            for i in range(m - 1):
                if needToJudge[i]:
                    flag = False
                    if A[i][j] < A[i + 1][j]:
                        needToJudge[i] = False
                    elif A[i][j] > A[i + 1][j]:
                        needToJudge, res = tep, res + 1
                        break
            if flag: return res  # we don't need to judge as there is no "True" in "needToJudge" array
        return res

strs1 = ["ca","bb","ac"]
strs2 = ["xc","yb","za"]
strs3 = ["zyx","wvu","tsr"]

print("Below are the required lexicographic deletions to get the string in order")
print(Solution.minDeletionSize(strs1))
print(Solution.minDeletionSize(strs2))
print(Solution.minDeletionSize(strs3))

print("Program finished")

