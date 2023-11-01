# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    leftVal = 0
    def sumOfLeftLeaves(root):
        if(root == None):
            return 0
        if(root.left != None and root.left.val):
            #print(root.left.val)
            #print(type(root.left.left))
            if(root.left.left == None and root.left.right == None):
                print(root.left.val)
                print("inside IF")
                Solution.leftVal += root.left.val
        #print(Solution.leftVal)
        Solution.sumOfLeftLeaves(root.left)
        Solution.sumOfLeftLeaves(root.right)

        return Solution.leftVal

    def inOrderInsert(numList, i, n):
        if(n-i<=0):
            return None
        if(numList[i] == None):
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


root = [3,9,20,None,None,15,7]
rootTree = Solution.inOrderInsert(root,0, len(root))
Solution.printTree(rootTree)
answer = Solution.sumOfLeftLeaves(rootTree)
print(answer)
