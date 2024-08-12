# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return 1 + Solution.minDepth(root.right)
        if root.right == None:
            return 1 + Solution.minDepth(root.left)
        return 1 + min(Solution.minDepth(root.left), Solution.minDepth(root.right))
    
        return 0
    @staticmethod
    def buildTree(root, index, n):
        if index >= n or root[index] == -1:
            return None
        node = TreeNode(root[index])
        node.left = Solution.buildTree(root, 2 * index + 1, n)
        node.right = Solution.buildTree(root, 2 * index + 2, n)
        return node
    def printTree(root):
        if root == None:
            return
        print(root.val)
        Solution.printTree(root.left)
        Solution.printTree(root.right)
        return
    
root = [3,9,20,-1,-1,15,7]
level = 0
n = len(root)
root = Solution.buildTree(root, level, n)
answer = Solution.minDepth(root)
Solution.printTree(root)
print(answer)  # Expected output: 2
        