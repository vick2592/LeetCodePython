class Solution:
    def reachingPoints(self, sx, sy, tx, ty, ans = False, count = 0):
        if ans == True:
            return ans
        if count > 10:
            return ans
        if sx == tx and sy == ty:
            ans = True
            print("True")
            return ans
        
        self.reachingPoints(sx, sx+sy, tx, ty, ans, count = count + 1)
        self.reachingPoints(sx+sy, sy, tx, ty, ans, count = count + 1)
    
sx = 1
sy = 1
tx = 3
ty = 5

sx = 1
sy = 1
tx = 2
ty = 2

answer = Solution()
print("The answer is: ", answer.reachingPoints(sx, sy, tx, ty))

