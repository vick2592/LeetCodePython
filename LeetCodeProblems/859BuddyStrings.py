class Solution:
    def buddyStrings(s, goal):
        testS = list(s)
        for x in range(len(s)):
            for y in range(x+1, len(s)):
                temp = testS[x]
                testS[x] = testS[y]
                testS[y] = temp
                test = ''.join(testS)
                if test == goal:
                    return True
                
        return False
    
s = "ab"
goal = "ba"
s = "ab"
goal = "ab"

answer = Solution.buddyStrings(s, goal)
print(answer)