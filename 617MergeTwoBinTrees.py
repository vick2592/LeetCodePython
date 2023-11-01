# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(root1, root2):
        sizeR1 = len(root1)
        sizeR2 = len(root2)

        if(sizeR1 > sizeR2):
            for i in range(sizeR2, sizeR1):
                root1.append(None)
        else:
            for j in range(sizeR1, sizeR2):
                root1.append(None)
        newRoot = []
        for k in range(len(root1)):
            if(root1[k] == None and root2[k] == None):
                newRoot.append(None)
                continue
            if(root1[k] == None):
                newRoot.append(root2[k])
                continue
            if(root2[k] == None):
                newRoot.append(root1[k])
                continue
            newRoot.append(root1[k] + root2[k])

        treeRoot = Solution.inOrderInsert(newRoot, 0, len(newRoot))
        return treeRoot

    def inOrderInsert(numList, i, n):
        if(n-i<=0):
            return None
        if(numList[i] ==None):
            return 
        node = TreeNode(numList[i])
        node.left = Solution.inOrderInsert(numList, 2*i+1, n)
        node.right = Solution.inOrderInsert(numList, 2*i+2, n)

        return node

    def printTree(node, level=0):
        if (node != None):
            Solution.printTree(node.left, level + 1)
            print(' ' * (4 * level) + '-> ' + str(node.val))
            Solution.printTree(node.right, level + 1)

#as a quick and dirty solution you can combine the lists first and then insert into binary tree and print.

root1 = [1,3,2,5]
root2 = [2,1,3,None,4,None,7]
answer = Solution.mergeTrees(root1,root2)
Solution.printTree(answer)
#tree1 = Solution.inOrderInsert(root1, 0, len(root1))
#tree2 = Solution.inOrderInsert(root2, 0, len(root2))
#mergedTree = Solution.mergeTrees(tree1, tree2)
#Solution.printTree(mergedTree)

