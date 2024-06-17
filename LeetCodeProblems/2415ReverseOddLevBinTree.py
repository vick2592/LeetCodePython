from copy import deepcopy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(root):
        rootCopy = deepcopy(root)
        topLevel = 0
        initialLen = len(root)
        while initialLen > 1:
            topLevel += 1
            initialLen = initialLen//2
        print(topLevel)
        for i in range(topLevel):
            if i % 2 == 1:
                rootBeg = 2**i - 1
                rootEnd = 2**(i+1) - 1
                print(rootBeg, rootEnd)
                rootCopy[rootBeg:rootEnd] = rootCopy[rootBeg:rootEnd][::-1]
                print(rootCopy)
                
        return root


root = [2,3,5,8,13,21,34]
ans = Solution.reverseOddLevels(root)
print(ans) #[2,3,5,8,13,21,34]
        

        