from math import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(root, queries):
        ansList = []
        n = len(root)
        print("Program Started")
        for q in queries:
            newRoot = Solution.inOrderInsert(root, 0, n)
            #Solution.printTree(newRoot, 0)
            #print("++++Seperation++++++")
            #Do a BFS to find node in query, since its never going to be first root you can check left and right and when found make it = None.
            nodeList = []
            allNodes = []
            nodeList.append(newRoot)
            allNodes.append(newRoot)
            #print("Current Node List is: ", nodeList)
            while (len(nodeList) > 0):
                curNode = nodeList[0]
                if(curNode.left != None):
                    if(curNode.left.val == q):
                        curNode.left = None
                        allNodes.append(curNode.left)
                    else:
                        nodeList.append(curNode.left)
                        allNodes.append(curNode.left)
            
                if(curNode.right != None):
                    if(curNode.right.val == q):
                        curNode.right = None
                        allNodes.append(curNode.right)
                    else:
                        nodeList.append(curNode.right)
                        allNodes.append(curNode.right)
                #print("Current Node value is: ", curNode.val)
                #allNodes.append(curNode.left)
                #allNodes.append(curNode.right)
                nodeList.pop(0)
            #for node in allNodes:
            #    if(node != None):
            #        print(node.val)
            #    else: 
            #        print(node)
            #This is a hack just for these examples but has bugs depending on other odd numbers like 5 and 7, which would come out as 3 layers by being upped by ceil
            #To go around this you would need to create another helper function that keeps dividing by 2 and keeping count until int() of value is 0. lev = count - 1
            #print("Bug case 1: ", ceil(log(5,2)), log(5,2))
            #print("Bug case 2: ", ceil(log(7,2)), log(7,2))
            #print("Bug case 3: ", floor(log(6,2)), log(6,2))
            #if(len(allNodes) % 2 == 0):
            #    lev = floor(log(len(allNodes),2))
            #else:
            #    lev = ceil(log(len(allNodes),2))
            #print("level is: ", lev)
            #print(len(allNodes), allNodes)
            #print("Current Node List is: ", nodeList)
            lev = 1
            loopVal = int(len(allNodes) / 2)
            while (loopVal > 0):
                loopVal = int(loopVal/2)
                lev += 1
            #Solution.printTree(newRoot, 0)
            ansList.append(lev-1)

        return ansList

    def inOrderInsert(numList, i, n):
        if(n-i<=0):
            return None
        if(numList[i] == None):
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


#Something is off with calculating the None in the first example and I am getting more than necessary for the log calculation of exponent given number and base. 
root = [1,3,4,2,None,6,5,None,None,None,None,None,7]
queries = [4]
root = [5,8,9,2,1,3,7,4,6]
queries = [3,2,4,8]
answer = Solution.treeQueries(root, queries)

print(answer)