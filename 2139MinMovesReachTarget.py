class Solution:
    def minMoves(target, maxDoubles):
        stepCount = 0

        while (target > 1):
            if ( target % 2 == 0 and maxDoubles > 0):
                target /= 2
                maxDoubles -= 1
                stepCount += 1
                continue
            if ( target % 2 == 0 and maxDoubles == 0):
                target -= 1
                stepCount += 1
                continue
            if ( target % 2 == 1 ):
                target -= 1
                stepCount += 1
                continue

        return stepCount

        #Think about making it backwards. Like count the numbers from max strategy while keeping track of current step going back to 1. 
        #Division from largest even number will cut the amount of distance from 1 by half. From there you must look into the evens and odds situation
        #Perhaps even see if you need to put two different conditions for even and odd. Ofcourse if need be impliment Dijkstra shortest path. 

target = 5
maxDoubles = 0

answer = Solution.minMoves(target, maxDoubles)
print(answer)

target2 = 19
maxDoubles2 = 2

answer2 = Solution.minMoves(target2, maxDoubles2)
print(answer2)

target3 = 10
maxDoubles3 = 4

answer3 = Solution.minMoves(target3, maxDoubles3)
print(answer3)