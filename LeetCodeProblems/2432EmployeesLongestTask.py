class Solution:
    def hardestWorker(n, logs):
        longest = 0
        longestEmp = -1
        curTime = 0
        for t in range(len(logs)):
            diff = logs[t][1] - curTime
            curTime = logs[t][1]
            if(diff > longest):
                longest = diff
                longestEmp = logs[t][0]

        return longestEmp
            





n = 26
logs = [[1,1],[3,7],[2,12],[7,17]]
answer = Solution.hardestWorker(n, logs)
print(answer)