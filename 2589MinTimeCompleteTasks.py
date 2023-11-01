class Solution:
    def findMinimumTime(tasks):
        minTime = 0

        for i in range(len(tasks)):
            tempStart = tasks[i][0]
            tempEnd = tasks[i][1]
            tempTime = tasks[i][2]
            for j in range(i+1, len(tasks)):
                tempCount = 0
                for k in range(tasks[j][0], tasks[j][1] + 1):
                    if(k >= tempStart and k <= tempEnd):
                        tempCount += 1
                tasks[j][2] = tasks[j][2] - tempCount
                if(tasks[j][2] < 0):
                    tasks[j][2] = 0

        for lst in tasks:
            minTime += lst[2]
        
        return minTime

tasks = [[1,3,2],[2,5,3],[5,6,2]]
answer = Solution.findMinimumTime(tasks)
print(answer)
