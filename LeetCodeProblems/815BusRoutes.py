class Solution:
    def numBusesToDestination(routes, source, target):
        startingRoute = 0
        queueDict = {}
        queueRoutes = []
        for i in range(len(routes)):
            if source in routes[i]:
                startingRoute = i
                for j in routes[i]:
                    if j == source:
                        continue
                    queueDict[j] = 1
                    queueRoutes.append(j)
                routes.pop(i)
                break
        
        while len(queueRoutes) > 0:
            testRoute = queueRoutes[0]
            queueRoutes.pop(0)
            routes2pop = []
            popCount = 0
            for i in range(len(routes)):
                if testRoute in routes[i]:
                    for j in routes[i]:
                        if j == testRoute:
                            continue
                        if j not in list(queueDict.keys()):
                            queueDict[j] = queueDict[testRoute] + 1
                            queueRoutes.append(j)
                    routes2pop.append(i)
            for k in routes2pop:
                routes.pop(k - popCount)
                popCount += 1
            
    
        if(target not in list(queueDict.keys())):
            return -1
        
        return queueDict[target]
    
routes = [[1,2,7],[3,6,7]]
source = 1
target = 6

# routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
# source = 15
# target = 12

answer = Solution.numBusesToDestination(routes, source, target)
print(answer)