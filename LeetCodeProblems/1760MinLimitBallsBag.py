class Solution:
    @staticmethod
    def minimumSize(nums, maxOperations):
        def canAchievePenalty(penalty):
            operations = 0
            for num in nums:
                if num > penalty:
                    # Calculate the number of operations needed to reduce num to penalty or less
                    operations += (num - 1) // penalty
            return operations <= maxOperations

        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            if canAchievePenalty(mid):
                high = mid
            else:
                low = mid + 1
        return low

# Example usage
nums1 = [9]
maxOperations1 = 2
nums2 = [2, 4, 8, 2]
maxOperations2 = 4

print(Solution.minimumSize(nums1, maxOperations1))  # Output: 3
print(Solution.minimumSize(nums2, maxOperations2))  # Output: 2