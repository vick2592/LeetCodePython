class Solution:
    def shortestCommonSupersequence(str1, str2):
        def isSubSq(str1, str2, str3):
            str1In = False
            str2In = False
            
            for i in range(len(str3)):
                for j in range(i, len(str3)):
                    testStr = str3[i:j+1]
                    if testStr == str1:
                        str1In = True
                    if testStr == str2:
                        str2In = True
                        
            return str1In and str2In
        
        if isSubSq(str1, str2, str1):
            return str1
        if isSubSq(str1, str2, str2):
            return str2
        dp = [str1+str2, str2+str1]
        def recursiveCheck(str1, str2, str3):
            if (len(str3) < len(str1) and len(str3) < len(str2)):
                return str1+str2
            
            if (isSubSq(str1, str2, str3) == True):
                minStr = str3
            else:
                minStr = str1 + str2
            for i in range(len(str3)):
                testStr = str3[:i] + str3[i+1:]
                #print(testStr)
                if testStr in dp:
                    continue
                else:
                    dp.append(testStr)
                    recursiveCheck(str1, str2, testStr)
            
        recursiveCheck(str1, str2, str1+str2)
        recursiveCheck(str2, str1, str2+str1)
        
        
         # Filter and sort the dp list
        valid_supersequences = [x for x in dp if isSubSq(str1, str2, x)]
        dp = sorted(valid_supersequences, key=len)
        print(dp)
        return dp[0]
       
        
    
str1 = "abac"
str2 = "cab"

str1 = "aaaaaaaa"
str2 = "aaaaaaaa"

answer = Solution.shortestCommonSupersequence(str1, str2)
print(answer)  # Expected output: "cabac"