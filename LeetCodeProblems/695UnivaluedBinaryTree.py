# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(root):
        firstNode = root[0]
        for n in root:
            if(n != firstNode):
                if(n != None):
                    return False
        return True
root = [1,1,1,1,1,None,1]
answer = Solution.isUnivalTree(root)
print(answer)