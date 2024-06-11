class Solution:
    def removeInvalidParentheses(s):
        def isValid(testS):
            count = 0
            for i in testS:
                if i == "(":
                    count += 1
                elif i == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        
        allValid = []
        minCount = 10**9+7
        
        def recCheck(st, count, level):
            nonlocal minCount
            if isValid(st) and level <= minCount and st not in allValid:
                allValid.append(st)
                minCount = min(minCount, level)
                print("selected: ", st, count, minCount, level)
            else:
                if count < len(st)-1:
                    count += 1
                    print(st, count, minCount, level)
                    recCheck(st, count, level)
                    if count < len(st):
                        level += 1
                        recCheck(st[:count-1] + st[count:], count, level)

        recCheck(s, 0, 0)
        

        return allValid
    
s = "(a)())()"
s = "()())()"
ans = Solution.removeInvalidParentheses(s)
print(ans) #["(a)()()", "(a())()"]
        