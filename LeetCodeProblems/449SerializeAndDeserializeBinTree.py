#Possibly combine with 1325 or reuse the code in 1325.
# Definition for a binary tree node.
#Note the difference on how self is called. When you call in order reset you set node be an instance of TreeNode
#Therefore, when you call node.left for example, self is implicit in object node. 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    serializedString = ""
    nodesList = []
    #Use a Breadth by first approach to encode and decode with depth first search. 
    #Remember BFS uses a queue first in first out while DFS is done via simple recursion. 
    def serialize(root):
        """Encodes a tree to a single string.
        """        
        Codec.nodesList.append(root)
        while(len(Codec.nodesList) != 0):
            root = Codec.nodesList.pop(0)
            if(root != None):
                if(root.val != None):
                    Codec.serializedString += str(root.val)
                    Codec.nodesList.append(root.left)
                    Codec.nodesList.append(root.right)
        return Codec.serializedString

    def deserialize(data):
        """Decodes your encoded data to tree.
        """
        rootNode = Codec.inOrderInsert(data, 0, len(data))
        return rootNode

        
    def inOrderInsert(numList, i, n):
        if(n-i<=0):
            return None
        node = TreeNode(numList[i])
        node.left = Codec.inOrderInsert(numList, 2*i+1, n)
        node.right = Codec.inOrderInsert(numList, 2*i+2, n)

        return node

    def printTree(node, level=0):
        if (node != None):
            Codec.printTree(node.left, level + 1)
            print(' ' * (4 * level) + '-> ' + str(node.val))
            Codec.printTree(node.right, level + 1)

# Your Codec object will be instantiated and called as such:
root = [2,1,3]
root = [1,2,3,2,0,2,4]
rootSize = len(root)
rootTree = Codec.inOrderInsert(root, 0, rootSize)
Codec.printTree(rootTree)
tree = Codec.serialize(rootTree)
print(tree)
ans = Codec.deserialize(tree)
Codec.printTree(ans)
