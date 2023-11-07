class Solution:
    def garbageCollection(garbage, travel):
        minCount = 0
        #Count for Metal
        mList = []
        idx = 0
        for h in garbage:
            if 'M' in h:
                minCount = minCount + h.count('M')
                mList.append(idx)
            idx += 1
        if len(mList) > 0:
            for i in range(mList[-1]):
                minCount += travel[i]
        
        #Count for Plastic
        gList = []
        idx = 0
        for h in garbage:
            if 'G' in h:
                minCount = minCount + h.count('G')
                gList.append(idx)
            idx += 1
        if len(gList) > 0:
            for i in range(gList[-1]):
                minCount += travel[i]
                
        #Count for Glass
        pList = []
        idx = 0
        for h in garbage:
            if 'P' in h:
                minCount = minCount + h.count('P')
                pList.append(idx)
            idx += 1
        if len(pList) > 0:
            for i in range(pList[-1]):
                minCount += travel[i]
        
        return minCount
    
garbage = ["G","P","GP","GG"]
travel = [2,4,3]

answer = Solution.garbageCollection(garbage, travel)
print(answer)