class Solution:
    def hasAlternatingBits(n):
        binString = Solution.decitoBin(n)
        #print(binString)
        answer = False
        firstBit = binString[0]
        enumBinString = list(enumerate(binString))
        endInd = enumBinString[-1][0]
        for ind, b in enumBinString:
            if (ind == endInd):
                answer = True
                break

            if binString[ind+1] == b:
                return False

            print("Current index, bit and binString: ", ind, b, binString)
        return answer

    def decitoBin(numb):
    # checking if the given number is greater than 1
        if numb > 1:
            # taking a empty string
            binastring = []
            # looping till number greater than 0 using while loop
            while(numb > 0):
                # We will get the last check bit whether it is set bit or not using % operator
                checkbit = numb % 2
                # converting this checkbit to string using str() function
                #checkbit = str(checkbit)
                # Concatenate this bit(can be 1 or 0 ) to the binstr.
                binastring.append(checkbit)
                # divide the number by 2
                numb = numb//2
        # reverse the binary string
        binastring = binastring[::-1]
        # return the resultant binary string
        return binastring


n = 5
answer = Solution.hasAlternatingBits(n)
print(answer) 