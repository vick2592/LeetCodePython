class Solution:
    def kSmallestPairs(nums1, nums2, k):
        ansList = []
        pairs = []
        for i in nums1:
            for j in nums2:
                tempPair = []
                tempPair.append(i)
                tempPair.append(j)
                pairs.append((tempPair, i + j))

        pairs = sorted(pairs, key = lambda x: x[1], reverse = False)
        #print(pairs)
        for testK in range(k):
            ansList.append(pairs[testK][0])
        return ansList
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

answer = Solution.kSmallestPairs(nums1, nums2, k)
print(answer)