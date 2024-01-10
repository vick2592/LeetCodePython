class Solution:
    def isRectangleCover(rectangles):
        lowestPair = [float("inf"), float("inf")]
        highestPair = [float("-inf"), float("-inf")]
        for i in range(len(rectangles)):
            if rectangles[i][0] < lowestPair[0]:
                lowestPair[0] = rectangles[i][0]
            if rectangles[i][1] < lowestPair[1]:
                lowestPair[1] = rectangles[i][1]
            if rectangles[i][2] > highestPair[0]:
                highestPair[0] = rectangles[i][2]
            if rectangles[i][3] > highestPair[1]:
                highestPair[1] = rectangles[i][3]
        # print(lowestPair, highestPair)
        allPoints = []
        for j in range(lowestPair[0], highestPair[0]):
            for k in range(lowestPair[1], highestPair[1]):
                allPoints.append([j,k])
        print(allPoints)
        
        for l in range(len(rectangles)):
            for m in range(rectangles[l][0], rectangles[l][2]):
                for n in range(rectangles[l][1], rectangles[l][3]):
                    if [m,n] in allPoints:
                        allPoints.remove([m,n])
                    else:
                        return False
            
        return True
    
rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
answer = Solution.isRectangleCover(rectangles)
print(answer)
