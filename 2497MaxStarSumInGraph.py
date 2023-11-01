class Solution:
    def maxStarSum(vals, edges, k):
        #enumVals = list(enumerate(vals))
        #enumVals.sort(key = lambda x: x[1])
        #print("This is enumVals: ", enumVals)
        edgeSum = {}
        for edge in edges:
            edgeSum[(edge[0],edge[1])] = vals[edge[0]]+ vals[edge[1]]
        print(edgeSum.items())
        sortedEdges = list(edgeSum.items())
        sortedEdges.sort(key = lambda x: x[1], reverse = True)
        print(sortedEdges)
        maxStarSum = 0
        prevEdge = ()
        for ind, i in list(enumerate(sortedEdges)):
            if k == 0:
                break
            if ind == 0:
                maxStarSum = maxStarSum + i[1]
                print(i)
                prevEdge = i[0]
                k -= 1
                continue
            if(i[0][0] in prevEdge):
                maxStarSum = maxStarSum + vals[i[0][1]]
                print(i)
                prevEdge = i[0]
                k -= 1
                continue
            if(i[0][1] in prevEdge):
                maxStarSum = maxStarSum + vals[i[0][0]]
                print(i)
                prevEdge = i[0]
                k -= 1
                continue


        return maxStarSum
vals = [1,2,3,4,10,-10,-20]
edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]]
k = 2

answer = Solution.maxStarSum(vals,edges,k)
print(answer)