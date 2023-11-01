from copy import deepcopy

class Solution:
    def minimumOneBitOperations(n):
        #"""
#        to flip the bits to turn the number to zero
        
#        Interpretation of Rules:
#        - recursive:
#            to turn a leading one of i bits to zero, the only way is to turn the i-1 bits to a leading one pattern
#            and to turn the i-1 bits leading zero to zero, the only way is to turn the i-2 bits to a leading one pattern
#            and so on, which is a recursive process
            
#            (10000.. -> 11000.. -> 01000..), (01000.. -> 01100.. -> 00100), ..., (..010 -> ..011 -> ..001 -> ..000)
            
#        - reversable:
        
#            Let's make some observations to check if there's any pattern:

#            - 2: 10 -> 11 -> 01 -> 00
#            - 4: 100 -> 101 -> 111 -> 110 -> 010 -> 011 -> 001 -> 000
#            - 8: 1000 -> 1001 -> 1011 -> 1010 -> 1110 -> 1111 -> 1101 -> 1100 -> 0100 -> (reversing 100 to 000) -> 0000
#            ...
            
#            based on the observation, turning every i bits leading one to zero, is turning the i-1 bits from 00.. to 10..
#            and then back to 00.., which is a reverable process, and with the recursive process we can conclude that
#            turning any length of 00..M-> 10.. is a reversable process
        
#        - all unique states:
#            since it is recursive and reversable, and we are flipping every bit between 1 and 0 programtically 10.. <-> 00..
#            we can conclude that every intermediate state in a process is unique (2**i unique states, so we need 2**i - 1 steps)
        
#                for i bits 10.. <-> 00.. - numer of operations f(i) = 2**i - 1
            
#            this also aligns with the observation above that f(i) = 2*f(i-1) - 1 (-1 for no operation needed to achieve the initial 000)
        
#        Process:
#        to turn any binary to 0, we can turning the 1s to 0s one by one from lower bit to higher bit
#        and because turning a higher bit 1 to 0, would passing the unique state including the lower bit 1s
#        we can reverse those operations needed for the higher bit 100.. to the unique state including the lower bit 1s
        
#        e.g. turning 1010100 to 0
#        - 1010(100) -> 1010(000), we will need 2**3 - 1 operations
#        - 10(10000) -> 10(00000), we will need (2**5 - 1) - (2**3 - 1) operations
#        we will be passing the state 10(10100), which is ready available from the last state
#        so we can save/reverse/deduct the operations needed for 1010(000) <-> 1010(100)
#        - ...
        
#            so for any binary, f(binary) would tell us how many operations we need for binary <-> 000..
#            and for any more 1s, 100{binary} we can regard it as a process of 100.. <-> 100{binary} <-> 000{000..}
#            which is 100.. <-> 000.. (2**i - 1) saving the operations 100{000..} <-> 100{binary} (f(binary))
#            = (2**i - 1) - f(last_binary)
            
#"""
        binary = format(n, "b")

        N, res = len(binary), 0
        print(N, binary)

        for i in range(1, N+1):
            if binary[-i] == "1": res = 2**i-1 - res

        return res
#Legacy Code I wrote that only works half the time use the above instead. 

#class Solution:
#    iterationList = []
#    count = 0 
#    def minimumOneBitOperations(n): 
#        bitList = Solution.decitoBin(n)
#        print(bitList)
#        extraCountNeeded = True
#        #if (bitList[-1]):
#        #    extraCountNeeded = False
#        extraCount = 0
#        allZero = False
#        loopLimit = 10000
#        listQueue = []
#        listQueue.append(bitList)
#        Solution.iterationList.append(bitList)
#        if (len(listQueue) != 0):
#            bitList = listQueue.pop(0)
#            #print("Current bitlist is: ", bitList)
#        #print("This is the Iteration List: ", Solution.iterationList)
#        allZero = Solution.checkIfZeroes(bitList)
#        if (allZero == True):
#            return Solution.count

#        while(allZero != True):
#            if (loopLimit < 0):
#                break
#            Solution.count += 1
#            loopLimit -= 1
#            if (len(listQueue) != 0):
#                #sorted(listQueue, key=lambda tup: tup[0], reverse = False)
#                listQueue.sort(key=lambda tup: tup[0], reverse=False)
#                print("Current Queue is: ", listQueue)
#                if(extraCountNeeded):
#                    if(len(listQueue) > 1):
#                        extraCount += 1
#                        print("The ExtraCount is: ", extraCount)
#                queueTup = listQueue.pop(0)
#                print("Current Queue tupple is: ", queueTup)
#                bitList = queueTup[1]
#            #print("Current iteration list is: ", Solution.iterationList)
#            #print("Current bitlist is: ", bitList)
#            opTwoList, opTwoCount = Solution.opTwo(bitList)
#            opOneList, opOneCount = Solution.opOne(bitList)
#            #if(opTwoCount in Solution.iterationList):
#            #    continue
#            #if(opOneCount in Solution.iterationList):
#            #    continue
#            #if (opTwoCount < opOneCount):
#            #print("Running opTwoList: ", opTwoList)
#            if(opTwoList not in Solution.iterationList):
#                Solution.iterationList.append(opTwoList)
#                listQueue.append((opTwoCount, opTwoList))
#                allZero = Solution.checkIfZeroes(opTwoList)
#                if (allZero == True):
#                    print("The ExtraCount is: ", extraCount)
#                    Solution.count = Solution.count - extraCount
#                    return Solution.count
#            #print("and then opOneList: ", opOneList)
#            if(opOneList not in Solution.iterationList):
#                Solution.iterationList.append(opOneList)
#                listQueue.append((opOneCount, opOneList))
#                allZero = Solution.checkIfZeroes(opOneList)
#                if (allZero == True):
#                    print("The ExtraCount is: ", extraCount)
#                    Solution.count = Solution.count - extraCount
#                    return Solution.count
#            print("--------------Countinuing Loop with count -------------------: ", Solution.count)
#            continue

#        print("The ExtraCount is: ", extraCount)
#        Solution.count = Solution.count - extraCount
#        return Solution.count

#    def checkIfZeroes(bitList):
#        bitTemp = []
#        allZeroBits = False
#        rightMostBit = len(bitList)-1
#        for ind, bit in list(enumerate(bitList)):
#            #Check if last index and bit == 0 then you successfully got to the end. 
#            if (ind == rightMostBit and bit == 0 and len(bitTemp) == 0):
#                allZeroBits = True
#                break
#            if bit == 1:
#                bitTemp.append(ind)
#        #print("Current One Bit array: ",  bitTemp)
#        if(allZeroBits == True):
#            return True
#        return False

#    def opTwo(bitList):
#        copyList = deepcopy(bitList)
#        bitTemp = []
#        for ind, bit in list(enumerate(copyList)):
#            if bit == 1:
#                bitTemp.append(ind)

#        if(len(bitTemp)==0):
#            return copyList, 0
#        indexBitCount = len(bitTemp)
#        leastSegnificantOneBitIdx = bitTemp[-1]
#        if (leastSegnificantOneBitIdx == 0):
#            return copyList, indexBitCount
#        if (copyList[leastSegnificantOneBitIdx - 1]):
#            copyList[leastSegnificantOneBitIdx - 1] = 0
#        else:
#            copyList[leastSegnificantOneBitIdx - 1] = 1

#        bitTemp = []
#        for ind, bit in list(enumerate(copyList)):
#            if bit == 1:
#                bitTemp.append(ind)

#        if(len(bitTemp)==0):
#            #print("Current Op2 copylist is: ", copyList)
#            binary_num = ""
#            for n in copyList:
#                binary_num += str(n)
#            decimal_num = int(binary_num, 2)
#            #print(binary_num, decimal_num)
#            return copyList, decimal_num
#        indexBitCount = len(bitTemp)
#        #print("Current Op2 copylist is: ", copyList)
#        binary_num = ""
#        for n in copyList:
#            binary_num += str(n)
#        decimal_num = int(binary_num, 2)
#        #print(binary_num, decimal_num)
#        return copyList, decimal_num

#    def opOne(bitList):
#        copyList = deepcopy(bitList)
#        #print(copyList)
#        endBit = len(bitList) - 1
#        if (copyList[endBit]):
#            copyList[endBit] = 0
#        else:
#           copyList[endBit] = 1
#        bitTemp = []
#        for ind, bit in list(enumerate(copyList)):
#            if bit == 1:
#                bitTemp.append(ind)
#        indexBitCount = len(bitTemp)
#        binary_num = ""
#        for n in copyList:
#            binary_num += str(n)
#        decimal_num = int(binary_num, 2)
#        return copyList, decimal_num

#    def decitoBin(numb):
#    # checking if the given number is greater than 1
#        if numb > 1:
#          # taking a empty string
#            binastring = []
#            # looping till number greater than 0 using while loop
#            while(numb > 0):
#                # We will get the last check bit whether it is set bit or not using % operator
#                checkbit = numb % 2
#                # converting this checkbit to string using str() function
#                #checkbit = str(checkbit)
#                # Concatenate this bit(can be 1 or 0 ) to the binstr.
#                binastring.append(checkbit)
#                # divide the number by 2
#                numb = numb//2
#        # reverse the binary string
#        binastring = binastring[::-1]
#        # return the resultant binary string
#        return binastring

n = 18
answer = Solution.minimumOneBitOperations(n)
print("The total count is: ", answer)