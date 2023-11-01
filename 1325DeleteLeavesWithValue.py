from functools import cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    loopCount = 0
    count = 0
    #Remember where you use @cache, even though it is not necessary here, when you placed it over removeLeafes it stored 
    #first iteration of the recursion and replayed it in each iteration of removeLeafNodes loop. 
    @cache
    def removeLeafNodes(root, target):
        n = Solution.nodeCount(root)
        while(n != 0):
            print("current iteration of n is: ",n)
            Solution.loopCount += 1
            Solution.removeLeafes(root,target)
            n /= 2
            n = int(n)
        print("Count is: ", n)

    def nodeCount(root):

        if(root != None):
            if(root.val != None):
                if(root.val == 0):
                    #print("Root val is: ", root.val)
                    #Solution.count = Solution.count + 0      
                    return 0
                else: 
                    #print("Else Root val is: ", root.val)
                    Solution.count += 1 
                    Solution.nodeCount(root.left)
                    Solution.nodeCount(root.right)        
                    return Solution.count
        return 0

    def removeLeafes(root, target):
        print(Solution.loopCount, root)
        #print(root)
        if (root != None):
            if(root.val != None):
                if(root.val == target):
                    print(root.val, target, root.right, root.left)
                #print("This iterations root.val: ", root.val)
                #node = root
                if((root.left == None or root.left.val == None) and (root.right == None or root.right.val == None) and root.val == target):
                    print("we reached target node: ", root.val)  
                    root.val = None
                    root.left = None
                    root.right = None
                    #del(root)
                    return

            Solution.removeLeafes(root.left, target)
            Solution.removeLeafes(root.right, target)

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

root = [1,2,3,2,None,2,4]
treeSize = len(root)
target = 2
rootNode = Solution.inOrderInsert(root, 0, treeSize)
Solution.printTree(rootNode)
Solution.removeLeafNodes(rootNode, target)
Solution.printTree(rootNode)

