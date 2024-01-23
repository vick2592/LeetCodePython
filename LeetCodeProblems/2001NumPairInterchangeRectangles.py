class Solution:
    def interchangeableRectangles(rectangles):
        count = 0
        pairList = []
        for x in range(len(rectangles)):
            for y in range(x+1, len(rectangles)):
                if rectangles[x][0] / rectangles[x][1] == rectangles[y][0] / rectangles[y][1] and (rectangles[x][0], rectangles[x][1], rectangles[y][0], rectangles[y][1]) not in pairList:
                    pairList.append((rectangles[x][0], rectangles[x][1], rectangles[y][0], rectangles[y][1]))
                    count += 1
                    
        print(pairList)
        return count
    
rectangles = [[4,8],[3,6],[10,20],[15,30]]
answer = Solution.interchangeableRectangles(rectangles)
print(answer)