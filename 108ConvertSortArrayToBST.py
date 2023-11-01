from math import floor

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#My Solution
class Solution:
    def sortedArrayToBST(nums):
        root = TreeNode(nums[int(floor(len(nums))/2)])
        midIdx = int(floor(len(nums))/2)
        newNums = []
        newNums.append(nums[int(floor(len(nums))/2)])
        for i in nums[:midIdx]:
            newNums.append(i)
        root.left = Solution.inOrderInsert(nums[:midIdx], 0, len(nums[:midIdx]))
        if(midIdx + 1 != len(nums)):
            for j in nums[midIdx+1:]:
                newNums.append(j)
            root.right = Solution.inOrderInsert(nums[midIdx+1:], 0, len(nums[midIdx+1:]))
        #root = Solution.inOrderInsert(newNums, 0, len(nums))
        print(newNums)

        return root

    def inOrderInsert(numList, i, n):
        if(n-i<=0):
            return None
        node = TreeNode(numList[i])
        node.left = Solution.inOrderInsert(numList, 2*i+1, n)
        node.right = Solution.inOrderInsert(numList, 2*i+2, n)

        return node

    def printTree(node, level=0):
        if (node != None):
            Solution.printTree(node.left, level + 1)
            print(' ' * (4 * level) + '-> ' + str(node.val))
            Solution.printTree(node.right, level + 1)
            

nums = [-10,-3,0,5,9]

answerRoot = Solution.sortedArrayToBST(nums)

Solution.printTree(answerRoot)
