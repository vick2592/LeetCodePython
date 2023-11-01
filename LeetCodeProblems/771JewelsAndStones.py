class Solution:
    def numJewelsInStones(jewels, stones):
        count = 0
        for c in stones:
            if c in jewels:
                count += 1

        return count


jewels = "aA"
stones = "aAAbbbb"

answer = Solution.numJewelsInStones(jewels, stones)

print("The number of jewels in a given collection of stones is: ", answer)
