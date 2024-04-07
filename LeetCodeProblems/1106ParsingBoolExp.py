class Solution:
    def parseBoolExpr(expression):
        stack = []
        test = expression.split('(')
        # print(test)
        for c in range(len(test)):
            test[c] = test[c].replace(')', '')
            test[c] = test[c].replace(',', '')

        #print(test)
        exp = False
        i = len(test)-2
        while i >= 0:
            if test[i] == '|':
                if i == len(test)-2:
                    expList = []
                    if test[i+1][0] == 't' or test[i+1][0] == 'f':
                        for k in test[i+1]:
                            if k == 't':
                                expList.append(True)
                            elif k == 'f':
                                expList.append(False)
                else:
                    expList.append(exp)
                if expList[0] == False:
                    testExp = False
                if expList[0] == True:
                    testExp = True
                for j in range(1, len(expList)):
                    testExp = testExp or expList[j]
                print("OR")
                exp = testExp
            if test[i] == '&':
                if i == len(test)-2:
                    expList = []
                    if test[i+1][0] == 't' or test[i+1][0] == 'f':
                        for k in test[i+1]:
                            if k == 't':
                                expList.append(True)
                            elif k == 'f':
                                expList.append(False)
                else:
                    expList.append(exp)
                if expList[0] == False:
                    testExp = False
                if expList[0] == True:
                    testExp = True
                for j in range(1, len(expList)):
                    testExp = testExp and expList[j]
                print("AND")
                exp = testExp
            if test[i] == '!':
                if i == len(test)-2:
                    expList = []
                    if test[i+1][0] == 't' or test[i+1][0] == 'f':
                        for k in test[i+1]:
                            if k == 't':
                                expList.append(True)
                            elif k == 'f':
                                expList.append(False)
                else:
                    expList.append(exp)
                if expList[0] == False:
                    testExp = False
                if expList[0] == True:
                    testExp = True
                # for j in range(1, len(test[i+1])):
                #     testExp = not testExp
                testExp = not testExp
                print("NOT")
                exp = testExp

            i -= 1
            print(exp, i, test[i])
        return exp
    
expression = "!(&(f,t))"
expression = "|(f,f,f,t)"
expression = "&(|(f))"
ans = Solution.parseBoolExpr(expression)
print(ans)  # Output: false
