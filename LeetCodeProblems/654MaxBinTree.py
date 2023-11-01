# Definition for a binary tree node.
from collections import Counter
from operator import countOf
from tkinter.tix import Tree


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:

    def printTree(node, level=0):
        if (node != None):
            printTree(node.left, level + 1)
            print(' ' * (4 * level) + '-> ' + str(node.val))
            printTree(node.right, level + 1)

    def constructMaximumBinaryTree(nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return None
        stk = []
        last = None
        for num in nums:
            while stk and stk[-1].val < num:
                last = stk.pop()
            node = TreeNode(num)
            if stk:
                stk[-1].right = node 
            if last:
                node.left = last
            stk.append(node)
            last = None
        return stk[0]

nums = [3,2,1,6,0,5]

# Using recursion to print the Binary Tree
def printTree(node, level=0):
    if (node != None):
        printTree(node.left, level + 1)
        print(' ' * (4 * level) + '-> ' + str(node.val))
        printTree(node.right, level + 1)

mbt654 = Solution.constructMaximumBinaryTree(nums)
printTree(mbt654)

print("try to do it again")

answer = Solution
rootNode = answer.constructMaximumBinaryTree(nums)
answer.printTree(rootNode)

