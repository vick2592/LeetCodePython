from symbol import continue_stmt

class Solution:
    def maxValue(events, k):
        earliestEventTime = 10**9+7 
        latestEventTime = 0 
        for i in events:
            if (i[0] < earliestEventTime ):
                earliestEventTime = i[0]
            if (i[1] > latestEventTime ):
                latestEventTime = i[1]

        print(earliestEventTime, latestEventTime)
        events.sort(key = lambda x: x[2], reverse = True)
        print(events)
        remainingK = k-1
        pq = events
        ans = 0
        pq.append(events[0])
        while (len(pq) > 0):
            schedule = [-1 for x in range(earliestEventTime, latestEventTime + 1)]
            #print("New schedule printed: ",schedule)
            curEvent = pq[0]
            pq.pop(0)
            schedule[curEvent[0]-1] = 1
            schedule[curEvent[1]-1] = 1
            remainingK = k-1
            print("New schedule printed: ",schedule)
            ansTemp = curEvent[2]
            for j in events:
                if (remainingK == 0):
                    if(ansTemp > ans):
                        ans = ansTemp
                    break
                if(j == curEvent):
                    continue
                if j[0] >= curEvent[0] and j[1] <= curEvent[1]:
                    continue
                if (schedule[j[0]-1] != -1 or schedule[j[1]-1] != -1):
                    continue 
                #print(schedule[j[0]],schedule[j[1]])
                schedule[j[0]-1] = 1
                schedule[j[1]-1] = 1
                print(schedule)
                ansTemp += j[2]
                remainingK -= 1
                print(remainingK)


        return ans
events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
k = 3
events = [[1,2,4],[3,4,3],[2,3,1]]
k = 2

answer = Solution.maxValue(events, k)
print(answer)