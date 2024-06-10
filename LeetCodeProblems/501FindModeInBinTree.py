# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(root):
        nodeDict = {}
        ansList = []
        for n in root:
            if n in nodeDict:
                nodeDict[n] += 1
            else:
                nodeDict[n] = 1
        maxFreq = max(nodeDict.values())
        for key, value in nodeDict.items():
            if value == maxFreq:
                ansList.append(key)
        return ansList

root = [1,-1,2,2]

print(Solution.findMode(root)) #2
        