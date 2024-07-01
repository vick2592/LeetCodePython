# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(root, targetSum):
        def buildTree(root, level, index):
            if index < len(root):
                if root[index] == 1001:
                    return None
                else:
                    node = TreeNode(root[index])
                    node.left = buildTree(root, level+1, 2*index+1)
                    node.right = buildTree(root, level+1, 2*index+2)
                    return node
            return None
        #Print the tree in a readable format
        def printTree(node, level):
            if node:
                printTree(node.right, level+1)
                print("   "*level + str(node.val))
                printTree(node.left, level+1)
        def countTree(node, targetSum, testCount):
            if node is None:
                return 0

            tempCount = testCount + node.val
            count = 1 if tempCount == targetSum else 0

            # Count paths including this node
            count += countTree(node.left, targetSum, tempCount)
            count += countTree(node.right, targetSum, tempCount)

            # Count paths not including this node (resetting the testCount)
            count += countTree(node.left, targetSum, 0)
            count += countTree(node.right, targetSum, 0)

            return count

        count = 0        
        rootNote = buildTree(root, 0, 0)
        printTree(rootNote, 0)
        count += countTree(rootNote, targetSum, 0)
        print("count", count)
        return count
    
root = [10,5,-3,3,2,1001,11,3,-2,1001,1]
targetSum = 8

ans = Solution.pathSum(root, targetSum)
print(ans)
# Expected: 3