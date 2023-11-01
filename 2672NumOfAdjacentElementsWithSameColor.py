class Solution:
    def colorTheArray(n, queries):
        answer = [0 for x in range(n)]
        answerList = [0 for z in range(len(queries))]
        idx = 0
        for q in queries:
            answer[q[0]] = q[1]
            #print(answer)
            testY = answer[0]
            sameCount = 0
            for y in range(1, len(answer)):
                if(answer[y] == testY and answer[y] != 0):
                    sameCount += 1
                testY = answer[y]
            answerList[idx] = sameCount
            idx += 1
        return answerList

n = 4
queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]
answer = Solution.colorTheArray(n,queries)
print(answer)