class Solution:
    def minSessions(tasks, sessionTime):
        count = 1
        tasks.sort(reverse=True)
        print(tasks)
        temp = sessionTime
        for n in tasks:
            temp -= n
            if temp < 0:
                temp = sessionTime
                count += 1
                temp - n
            
        return count


tasks = [3,1,3,1,1]
sessionTime = 8

answer = Solution.minSessions(tasks, sessionTime)

print(answer)