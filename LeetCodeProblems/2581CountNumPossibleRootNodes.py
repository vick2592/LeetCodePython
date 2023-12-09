from copy import deepcopy

class Solution:
    def rootCount(edges, guesses, k):
        count = 0
        nodes = [n[0] for n in edges] + [n[1] for n in edges]
        nodes = list(set(nodes))
        #print(nodes)
        trees = []
        for n in nodes:
            tempTree = []
            edgesCloned = deepcopy(edges)
            curNodes = [n]
            noMatch = True
            while(len(edgesCloned) > 0):
                for e in range(len(edgesCloned)):
                    if edgesCloned[e][0] in curNodes:
                        curNodes.append(edgesCloned[e][0])
                        curNodes.append(edgesCloned[e][1])
                        tempTree.append(edgesCloned[e])
                        edgesCloned.remove(edgesCloned[e])
                        noMatch = False
                        break
                    elif edgesCloned[e][1] in curNodes:
                        curNodes.append(edgesCloned[e][1])
                        curNodes.append(edgesCloned[e][0])
                        tempTree.append([edgesCloned[e][1], edgesCloned[e][0]])
                        edgesCloned.remove(edgesCloned[e])
                        noMatch = False
                        break
                if noMatch == True:
                    break
            if noMatch == False:        
                trees.append(tempTree)    
        
        print(trees)
        
        correctGuesses = {}
        for t in trees:
            gCount = 0
            for g in guesses:
                if g in t:
                    gCount += 1
            correctGuesses[t[0][0]] = gCount
            
        print(correctGuesses)
        
        for c in correctGuesses:
            if correctGuesses[c] >= k:
                count += 1
        return count
    
edges = [[0,1],[1,2],[1,3],[4,2]]
guesses = [[1,3],[0,1],[1,0],[2,4]]
k = 3

edges = [[0,1],[1,2],[2,3],[3,4]]
guesses = [[1,0],[3,4],[2,1],[3,2]]
k = 1

answer = Solution.rootCount(edges, guesses, k)
print(answer)
