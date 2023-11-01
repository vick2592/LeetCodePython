class Solution:
    def edgeScore(edges):
        tempMap = {}
        for i in range(len(edges)):
            if(tempMap[edges[i]]):
                tempMap[edges[i]]) += i
                continue
            tempMap[edges[i]] = i
            
        answer = []
        highest = 0
       
        for k,v in tempMap.items():
            if(v > highest):
                highest = v;
                
        for k,v in tempMap.items():
            if(v == highest):
                answer.append((k, v))
                
        answer = sorted(answer, key = Lambda x: x[1], reverse = True)
        return answer[0][0]
        
edges = [1,0,0,0,0,7,7,5]
answer = Solution.edgeScore(edges)
print(answer)