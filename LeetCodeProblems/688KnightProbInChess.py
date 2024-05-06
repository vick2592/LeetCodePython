class Solution:
    def knightProbability(n, k, row, column):
        if k == 0:
            return 1
        queueL = []
        queueL.append([row, column, 0])
        total = 0
        inCount = 0
        while (len(queueL) > 0):
            cur = queueL.pop(0)
            if cur[2] == k:
                continue
            #Go to the right and down
            if cur[0] + 1 < n and cur[1] + 2 < n:
                queueL.append([cur[0] + 1, cur[1] + 2, cur[2] + 1])
                inCount += 1
                total += 1
            else:
                total += 1
            #Go to the right and up
            if cur[0] - 1 >= 0 and cur[1] + 2 < n:
                queueL.append([cur[0] - 1, cur[1] + 2, cur[2] + 1])  
                inCount += 1
                total += 1
            else:
                total += 1
            #Go to the left and down
            if cur[0] + 1 < n and cur[1] - 2 >= 0:
                queueL.append([cur[0] + 1, cur[1] - 2, cur[2] + 1])   
                inCount += 1
                total += 1
            else:
                total += 1
            #Go to the left and up
            if cur[0] - 1 >= 0 and cur[1] - 2 >= 0:
                queueL.append([cur[0] - 1, cur[1] - 2, cur[2] + 1])    
                inCount += 1
                total += 1
            else:
                total += 1
            #Go to the up and right
            if cur[0] - 2 >= 0 and cur[1] + 1 < n:
                queueL.append([cur[0] - 2, cur[1] + 1, cur[2] + 1])    
                inCount += 1
                total += 1
            else:
                total += 1
            #Go to the up and left
            if cur[0] - 2 >= 0 and cur[1] - 1 >= 0:
                queueL.append([cur[0] - 2, cur[1] - 1, cur[2] + 1])   
                inCount += 1
                total += 1
            else:
                total += 1
            #Go to the down and right
            if cur[0] + 2 < n and cur[1] + 1 < n:
                queueL.append([cur[0] + 2, cur[1] + 1, cur[2] + 1])  
                inCount += 1
                total += 1
            else:
                total += 1
            #Go to the down and left
            if cur[0] + 2 < n and cur[1] - 1 >= 0:
                queueL.append([cur[0] + 2, cur[1] - 1, cur[2] + 1])
                inCount += 1
                total += 1
            else:
                total += 1
            ans = (inCount/total)**k
        return ans
            
    
n = 1
k = 0
row = 0
column = 0
print(Solution.knightProbability(n, k, row, column)) #0.0625