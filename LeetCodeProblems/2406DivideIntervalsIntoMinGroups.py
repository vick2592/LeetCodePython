from copy import deepcopy

class Solution:
    def minGroups(intervals):
        copyIntervals = deepcopy(intervals)
        IntervalsDict = {}
        numbersList = []
        uniqueIntervals = []

        for i in intervals:
            numbersList.append(i[0])
            numbersList.append(i[1])
        
        for n in numbersList:
            IntervalsDict[n] = 0

        for n in numbersList:
            IntervalsDict[n] += 1

        for k,v in IntervalsDict.items():
            if v > 1:
                uniqueIntervals.append(k)


        print(uniqueIntervals)
        return len(uniqueIntervals)
intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]

#Count how many numbers are common and that is your answer to how many groups need to be created. 

answer = Solution.minGroups(intervals)
print(answer)

