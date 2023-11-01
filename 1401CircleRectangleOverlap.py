class Solution:
    def checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2):
        if (xCenter >= x1 and xCenter <= x2 and yCenter >= y1 and yCenter <= y2):
            return True
        elif (xCenter + radius >= x1 and xCenter + radius <= x2 and yCenter >= y1 and yCenter <= y2):
            return True
        elif (yCenter + radius >= y1 and yCenter + radius <= y2 and xCenter >= x1 and xCenter <= x2):
            return True
        else:
            return False
    
radius = 1
xCenter = 0
yCenter = 0
x1 = 1
y1 = -1
x2 = 3
y2 = 1

radius = 1
xCenter = 1
yCenter = 1
x1 = 1
y1 = -3
x2 = 2
y2 = -1

answer = Solution.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)
print(answer)