from functools import cache
from copy import deepcopy
import itertools

class Solution:
    def canEat(self, candiesCount, queries):
        prefix_sum = [0] + list(itertools.accumulate(candiesCount))
        print(prefix_sum)
        result = []

        for favoriteType, favoriteDay, dailyCap in queries:
            min_candies = prefix_sum[favoriteType] // dailyCap
            max_candies = prefix_sum[favoriteType + 1]

            result.append(min_candies <= favoriteDay < max_candies)

        return result
#My Failed Recursive Solution and iterative solution are commented out due to them not being the correct approach for this.
#Recursive Solution brings exponential time complexity and this can be solved via prefix sum which is what I was doing initially. 
    # ans = []
    # def canEat(self, candiesCount, queries):
    #     for j in range(len(queries)):
    #         self.ans.append(False)
    #     @cache
    #     def recurseCandy(curCount, query, curCandy, curDay, curCap, startCap):
    #         curCount = list(curCount)  # Convert tuple back to list
    #         query = list(query)  # Convert tuple back to list
    #         if curDay < query[1]:
    #             return # Add condition to prevent infinite recursion
    #         print("curCount, curCandy, query, curDay, curCap, startCap: " , curCount, curCandy, query, curDay, curCap, startCap)

    #         if (query[0] == curCandy and query[1] == curDay):
    #             if self.ans[query[3]] == False:
    #                 self.ans[query[3]] = True
    #             return 
            
    #         num = curCount[curCandy] - startCap
    #         count = 1
    #         if num < 0 and curCandy + 1 < len(curCount):
    #             while (num < 0):
    #                 if curCandy + count >= len(curCount):
    #                     count -= 1
    #                     break
    #                 num += curCount[curCandy+count]
    #                 count += 1
    #             curCount[curCandy+count] += num
    #             recurseCandy(tuple(curCount), tuple(query), curCandy+count, curDay+1, curCap, startCap)
    #             if startCap + 1 < curCap:
    #                 recurseCandy(tuple(curCount), tuple(query), curCandy+count, curDay+1, curCap, startCap + 1)
    #         recurseCandy(tuple(curCount), tuple(query), curCandy, curDay+1, curCap, startCap)
    #         if startCap + 1 < curCap:
    #             recurseCandy(tuple(curCount), tuple(query), curCandy, curDay+1, curCap, startCap + 1)       

    #     for i in range(len(queries)):
    #         updatedQuery = deepcopy(queries[i])
    #         updatedQuery.append(i)
    #         recurseCandy(tuple(candiesCount), tuple(updatedQuery), 0, 0, queries[i][2], 1)

    #     return self.ans
    
candiesCount = [7,4,5,3,8]
queries = [[0,2,2],[4,2,4],[2,13,1000000000]]

candiesCount = [5,2,6,4,1]
queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]

answer = Solution()
result = answer.canEat(candiesCount, queries)
print(result)

            
        # ans = []
        # for i in range(len(queries)):
        #     query = queries[i]
        #     favoriteType = query[0]
        #     favoriteDay = query[1]
        #     dailyCap = query[2]
        #     candyCount = 0
        #     rangeC = []
        #     for c in range(len(candiesCount)):
        #         if c < favoriteType:
        #             candyCount += candiesCount[c]
        #         else:
        #             rangeC.append(candyCount+1)
        #             candyCount += candiesCount[c]
        #             rangeC.append(candyCount)
        #             break
        #     print(rangeC)
        #     x = 0
        #     daysLeft = favoriteDay
        #     for j in range(1, dailyCap+1):
        #         testCount = 0
        #         while(daysLeft > 0):
        #             testCount += j;
        #             daysLeft -= 1
        #             if(testCount >= rangeC[0] and testCount <= rangeC[1]):
        #                 ans.append(True)
        #                 x = 1
        #                 break
                    
        #         if x == 1:
        #             break
        #     if x == 0:
        #         ans.append(False)
                