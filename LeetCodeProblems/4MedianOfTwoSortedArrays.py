class Solution:
    def findMedianSortedArrays(nums1, nums2):
        testList = nums1 + nums2
        print(testList)

        if(len(testList) % 2 == 1):
            index = (len(testList) // 2)
            print(index)
            median = testList[index]
            return median
        indexEven = (len(testList) // 2) - 1
        medianEven = (testList[indexEven] + testList[indexEven + 1])/2
        return medianEven

nums1 = [1,2]
nums2 = [3,4]

answer = Solution.findMedianSortedArrays(nums1, nums2)
print(answer)