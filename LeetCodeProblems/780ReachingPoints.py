class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        print(sx,sy,tx,ty)
        if sx > tx or sy > ty:
            return False
        if sx == tx and sy == ty:
            print("Match Found")
            return True
        
        ans = self.reachingPoints(sx, sx+sy, tx, ty)
        if ans == True:
            return True
        ans = self.reachingPoints(sx+sy, sy, tx, ty)
        if ans == True:
            return True
        
        return ans  
    
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

