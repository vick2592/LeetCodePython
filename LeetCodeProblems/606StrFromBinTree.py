#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    treestr = ""
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
    def preorder(self, node):
        if node is None:
            return ""
        elif node.left is None and node.right is None:
            return str(node.val)
        elif node.left is None and node.right is not None:
            return str(node.val) + "()" + "(" + self.preorder(node.right) + ")"
        elif node.right is None:
            return str(node.val) + "(" + self.preorder(node.left) + ")"
        else:
            return str(node.val) + "(" + self.preorder(node.left) + ")" + "(" + self.preorder(node.right) + ")"
            

    
root = [1,2,3,4]
root = [1,2,3,None,4]
ans = Solution()
Noderoot = ans.inOrderInsert(root, 0, len(root))
ans.printTree(Noderoot)
test = ans.preorder(Noderoot)
print(ans.treestr)
print(test)
