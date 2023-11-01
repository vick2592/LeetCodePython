class Solution:
    def divisorSubstrings(num, k):
        numString = str(num)
        kBeauty = 0
        #print(numString)
        numList = [c for c in numString]
        numEnum = list(enumerate(numList))
        endIndex = numEnum[-1][0]
        #print(numList)
        for i, c in numEnum:
            if (i+k == endIndex+1):
                intSubString = int(numString[i:])
                #print(intSubString)
                if(intSubString == 0):
                    break
                if(num % intSubString == 0):
                    kBeauty += 1
                break
            numberString = int(numString[i:i+k])
            if ( numberString == 0):
                continue
            if (num % numberString == 0):
                kBeauty += 1

        return kBeauty

num = 240
k = 2

answer = Solution.divisorSubstrings(num, k)
print("The kBeauty of given number is: ", answer)

num1 = 430043
k1 = 2

answer1 = Solution.divisorSubstrings(num1, k1)
print("The kBeauty of given number is: ", answer1)