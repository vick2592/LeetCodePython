#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    treestr = ""
    rootFound = TreeNode()
    def inOrderInsert(self, numList, i, n):
        if(n-i<=0):
            return None
        if(numList[i] == None):
            return 
        node = TreeNode(numList[i])
        node.left = self.inOrderInsert(numList, 2*i+1, n)
        node.right = self.inOrderInsert(numList, 2*i+2, n)

        return node
    def printTree(self, node, level=0):
        if (node != None):
            self.printTree(node.left, level + 1)
            print(' ' * (4 * level) + '-> ' + str(node.val))
            self.printTree(node.right, level + 1)
            
    def searchBST(self, root, val):
        if root == None:
            return None
        if root.val == val:
            self.rootFound = root
            return 
        if root.left != None:
            self.searchBST(root.left, val)
        if root.right != None:
            self.searchBST(root.right, val)
        
        return self.rootFound

            
root = [4,2,7,1,3]
val = 2
root = [4,2,7,1,3]
val = 5
ans = Solution()
Noderoot = ans.inOrderInsert(root, 0, len(root))

ans.printTree(ans.searchBST(Noderoot, val))

