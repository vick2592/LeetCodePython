class Solution:
    def areConnected(n, threshold, queries):
        
        #Building a map that stores all connected nodes of a node
        graph = {}
        for x in range(1, n+1):
            for y in range(x+1, n+1):
                if x not in graph:
                    graph[x] = []
                if y not in graph:
                    graph[y] = []
                for z in range(1, n+1):
                    if x % z == 0 and y % z == 0 and z > threshold:
                        graph[x].append(y)
                        graph[y].append(x)
        print(graph)
        
        #Traversing the graph via a quewue to see if each query is connected
        ans  = []
        for i in range(len(queries)):
            queue = [queries[i][0]]
            visited = set()
            connected = False
            while queue:
                node = queue.pop(0)
                visited.add(node)
                if queries[i][1] in visited:
                    connected = True
                    break
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            ans.append(connected)
            
        #Returning a list of booleans indicating if each query is connected
        return ans
n = 6
threshold = 2
queries = [[1,4],[2,5],[3,6]]
        
answer = Solution.areConnected(n, threshold, queries)
print(answer)  # Output: [true,true,true]

