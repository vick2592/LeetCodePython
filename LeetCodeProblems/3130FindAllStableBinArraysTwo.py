class Solution:
    def numberOfStableArrays(zero, one, limit):
        dp = []  # This will store all unique combinations
        stableDP = []  # This will store all stable combinations
        modulo = 10**9 + 7

        # Recursive function to generate all combinations
        def recursiveAdd(currentArray, zerosLeft, onesLeft):
            if zerosLeft == 0 and onesLeft == 0:
                # Base case: no zeros or ones left to place, check if the currentArray is stable
                if currentArray not in dp:
                    dp.append(currentArray[:])  # Add a copy of currentArray to dp
                    if checkStable(currentArray, limit) and currentArray not in stableDP:
                        stableDP.append(currentArray[:])
                return

            if zerosLeft > 0:
                # Choose a position for a zero and recurse
                recursiveAdd(currentArray + [0], zerosLeft - 1, onesLeft)

            if onesLeft > 0:
                # Choose a position for a one and recurse
                recursiveAdd(currentArray + [1], zerosLeft, onesLeft - 1)

        def checkStable(initArray, limit):
            # Check if every subarray of size > limit contains both 0 and 1
            for i in range(len(initArray)):
                for j in range(i + limit + 1, len(initArray) + 1):
                    subArray = initArray[i:j]
                    if 0 not in subArray or 1 not in subArray:
                        return False
            return True

        # Start the recursion with an empty array and the full count of zeros and ones
        recursiveAdd([], zero, one)
        print(stableDP)
        # Return the count of stable arrays modulo 10**9 + 7
        return len(stableDP) % modulo

    
zero = 3
one = 3
limit = 2

ans = Solution.numberOfStableArrays(zero, one, limit)
print(ans)
        