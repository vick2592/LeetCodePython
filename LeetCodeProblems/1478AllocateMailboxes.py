class Solution:
    def minDistance(houses, k):
        def distanceCount(houses, mailbox):
            totalDistance = 0
            for house in houses:
                if house not in mailbox:
                    minDistance = float('inf')
                    for m in mailbox:
                        minDistance = min(minDistance, abs(house - m))
                    totalDistance += minDistance
            return totalDistance

        def recursiveBoxes(houses, k, index, mailbox):
            if k == 0:
                return distanceCount(houses, mailbox)
            if index > houses[-1]:
                return float('inf')
            # Place a mailbox at the current house
            mailbox.append(index)
            placeMailbox = recursiveBoxes(houses, k - 1, index + 1, mailbox)
            mailbox.pop()
            # Skip the current house
            skipMailbox = recursiveBoxes(houses, k, index + 1, mailbox)
            return min(placeMailbox, skipMailbox)

        return recursiveBoxes(houses, k, 0, [])

houses = [1,4,8,10,20]
k = 3

# houses = [2,3,5,12,18]
# k = 2

answer = Solution.minDistance(houses, k)
print(answer)  # Expected output: 5