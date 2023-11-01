# Definition for a binary tree node.
from math import sqrt, floor 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
         
class Solution:
    def isSubtreeIterevly(rootList, subList):
        rootSubDict = {}
        listSize = len(rootList)
        binaryLevel = 0
        for n in range(listSize):
            testLevel = 2
            testLevel = testLevel ** n
            if(testLevel > listSize):
                binaryLevel = n
                break
        print("Binary Level is: ", binaryLevel)
        nodeIndex = 0
        #Get all the left elements
        while(binaryLevel != 0):
            curList = []
            curList.append(rootList[nodeIndex])
            for n in range(nodeIndex, listSize):
                if(n * 2 + 1 >= listSize):
                    break;
                curList.append(rootList[n * 2 + 1])
                if(n * 2 + 2 >= listSize):
                    break
                curList.append(rootList[n * 2 + 2])
            rootSubDict[nodeIndex] = curList
            binaryLevel -= 1
            nodeIndex += 1
        print(rootSubDict)
        inRoot = False
        for i in rootSubDict.items():
            if subList in i:
                inRoot = True
        
        return inRoot
    def isSubtree(rootNode, subRoot):
        #Initially find the roots that are equal
        if(rootNode == None and subRoot == None):
            return True
        if(rootNode != None and subRoot == None):
            return False
        if(rootNode == None and subRoot != None):
            return False
        if(rootNode.val != subRoot.val):
            inRoot = Solution.isSubtree(rootNode.left, subRoot)
            #if(inRoot == True):
            #    return True
            inRoot = Solution.isSubtree(rootNode.right, subRoot)
            if(inRoot == True):
                return True
            return False
        if(rootNode.val == subRoot.val):
            inRoot = Solution.isSubtree(rootNode.left, subRoot.left)
            inRoot = Solution.isSubtree(rootNode.right, subRoot.right)
            print(rootNode.val, subRoot.val)
            return True

        return inRoot

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

root = [3,4,5,1,2]
#root = [3,4,5,1,2,None, None, None, None, 0]
subRoot = [4,1,2]
rootSize = len(root)
subSize = len(subRoot)
answer = Solution
rootTree = answer.inOrderInsert(root, 0, rootSize)
subTree = answer.inOrderInsert(subRoot, 0, subSize)
answer.printTree(rootTree)
answer.printTree(subTree)
inRoot = answer.isSubtree(rootTree, subTree)
print("inRoot value: ", inRoot)

inRootList = answer.isSubtreeIterevly(root, subRoot)
print("inRootList value: ", inRootList)