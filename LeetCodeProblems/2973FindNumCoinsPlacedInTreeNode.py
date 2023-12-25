class Solution:
    def placedCoins(edges, cost):
        ans = {}
        nodes = []
        for i in edges:
            if i[0] not in nodes:
                nodes.append(i[0])
            if i[1] not in nodes:
                nodes.append(i[1])
        #print(nodes)
        for n in nodes:
            subTreeList = [n]
            queueTracker = [n]
            while(len(queueTracker) > 0):
                for i in edges:
                    if i[0] == queueTracker[0] and i[1] not in subTreeList:
                        queueTracker.append(i[1])
                        subTreeList.append(i[1])
                queueTracker.pop(0)
                #print("Current queue is:", queueTracker)
            print(subTreeList)
            testNode = subTreeList[0]
            if (len(subTreeList) < 3):
                ans[testNode] = 1
            else:
                testCost = 1
                testTree = []
                for k in subTreeList:
                    testTree.append(cost[k])
                testTree = sorted(testTree, reverse = True)
                print("Sorted testTree is: ", testTree)
                testCost = testCost * testTree[0] * testTree[1] * testTree[2]
                if testCost < 0:
                    ans[testNode] = 0
                else:
                    ans[testNode] = testCost
            subTreeList.clear()
            queueTracker.clear()
        return list(ans.values())

edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]]
cost = [1,4,2,3,5,7,8,-4,2]

answer = Solution.placedCoins(edges, cost)
print(answer)
