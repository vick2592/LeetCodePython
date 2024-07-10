# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inOrderInsert(self, numList, i, n):
        if i >= n or numList[i] is None:
            return None
        node = TreeNode(numList[i])
        node.left = self.inOrderInsert(numList, 2*i+1, n)
        node.right = self.inOrderInsert(numList, 2*i+2, n)
        return node

    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
    def printTree(self, node, level=0):
        if (node != None):
            self.printTree(node.left, level + 1)
            print(' ' * (4 * level) + '-> ' + str(node.val))
            self.printTree(node.right, level + 1)

    def levelOrderTraversal(self, root):
        if not root:
            return []
        result, queue = [], [root]
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

# Example usage
root = [4,2,7,1,3,6,9]
classTree = Solution()
ans = classTree.inOrderInsert(root, 0, len(root))
classTree.printTree(ans)
invertedRoot = classTree.invertTree(ans)
ansArray = classTree.levelOrderTraversal(invertedRoot)
print(ansArray)

    


