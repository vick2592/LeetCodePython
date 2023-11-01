class Solution:
    def maxProduct(nums):
        enumNums = list(enumerate(nums))
        answerList = []
        endIndex = enumNums[-1][0]
        def getProductSum(list):
            productSum = 0
            if len(list) == 0:
                return 0
            for i in list:
                if productSum == 0:
                    productSum += i
                    continue
                productSum *= i
            return productSum
        for i, n in enumNums:
            #print(n)
            #print("The answer List during each iteration is: ", answerList)
            curList = []
            test = []
            if i == endIndex :
                if n != 0 and n > 0:
                    test = []
                    test.append(n)
                    #print("The test array at index -1 is: ", test)
                    if getProductSum(test) > getProductSum(answerList):
                        answerList = test
                break

            for j in range(i, endIndex + 1):
                curList.append(enumNums[j][1])
                #print(curList)
                #print(getProductSum(curList))
                curListProd = int(getProductSum(curList))
                curAnswerProd = int(getProductSum(answerList))
                #print("The current List Product is: ", curListProd)
                #if (curListProd > curAnswerProd):
                    #print("Current answer list has been changed.")
                    #answerList = curList

                #if ( curListProd < curAnswerProd):
                #    print("The Current List Product is less than the Cur Answer Product")
                if ( curListProd > curAnswerProd ):
                    print("The Current list is greater than the answer product")
                    #Remember that when you are assigning one list to another they equal the same memory address so answerList would always
                    #equal curList unless you make a copy of it pre assignment. One way to do that is with slicing [:] or copy() method.
                    answerList = curList[:]
                #print("The currentAnswerList is: ", answerList)
        
        print("The answer List is: ", answerList)
        answer = getProductSum(answerList)
        return answer 



nums = [2,3,-2,4]

answer = Solution.maxProduct(nums)
print("The maxProduct of give list of nums is: ", answer)


