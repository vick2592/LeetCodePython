class Solution:
    def isTransformable(s, t):
        dp = [s]
        queue = [s]
        
        while queue:
            sTest = queue.pop(0)
            if sTest == t:
                return True
            
            for x in range(len(s)):
                for y in range(x, len(s)):
                    opStr = ""
                    sL = [c for c in sTest]
                    testSl = sL[:x] + sorted(sL[x:y+1]) + sL[y+1:]
                    opStr = "".join(testSl)
                    if opStr not in dp:
                        dp.append(opStr)
                        queue.append(opStr)

        return False
    
s = "12345"
t = "12435"
# s = "34521"
# t = "23415"

ans = Solution.isTransformable(s, t)
print(ans)  # Output: True
