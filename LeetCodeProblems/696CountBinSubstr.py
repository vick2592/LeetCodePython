class Solution:
    def countBinarySubstrings(s):
        subStr = []
        for x in range(len(s)):
            test = []
            print("test is emprty", test)
            for y in range(x, len(s)):
                test.append(s[y])
                subStr.append(tuple(test))
                print(test)
        #subStr = sorted(subStr, key=len)            
        print(subStr)
        minStr = []
        for ss in subStr:
            countZero = 0
            countOne = 0
            for b in ss:
                if b == '0':
                    countZero += 1
                elif b == '1':
                    countOne += 1
            if countZero != countOne:
                continue
            print(countZero, countOne)
            print(ss)
            init = ss[0]
            initCount = countZero
            if ss[0] == '1':
                initCount = countOne
            gotStr = True
            for c in range(initCount):
                if ss[c] != init:
                    gotStr = False
            if gotStr:
                minStr.append(ss)
                
        print("The minStr is: ", minStr)
        

        ans = len(minStr)
        return ans
    
s = "00110011"
answer = Solution.countBinarySubstrings(s)
print(answer)

