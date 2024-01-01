class Solution:
    def rotatedDigits(n):
        ans = 0
        for i in range(1,n+1):
            org = list((j for j in str(i)))
            test = []
            invalid = False
            for k in range(len(org)):
                if (org[k] == "0" or org[k] == "1" or org[k] == "8"):
                    test.append(org[k])
                elif (org[k] == "2"):
                    test.append("5")
                elif (org[k] == "5"):
                    test.append("2")
                elif (org[k] == "6"):
                    test.append("9")
                elif (org[k] == "9"):
                    test.append("6")
                else:
                    invalid = True
                    
            if (invalid):   
                continue        
            testOrg = "".join(org)
            testTest = "".join(test)
            print(testOrg, testTest)
            if (testOrg != testTest):
                ans += 1
                
        return ans;

n = 10
answer = Solution.rotatedDigits(n)
print(answer)

        