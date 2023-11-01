class Solution:
    def findJudge(n, trust):
        judge = -1
        for p in range(1, n+1):
            inP = True
            for pair in trust:
                if p == pair[0]:
                    inP = False
                    break
            if inP == True:
                judge = p
                return judge
        return judge
n = 3 
trust = [[1,3],[2,3]]
answer = Solution.findJudge(n, trust)
print(answer)