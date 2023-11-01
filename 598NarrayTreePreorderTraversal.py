# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(root):
        prevNode = Node
        PrevChildren = []
        children = []
        rootNode = Node
        allNodes = []  # all nodes of the tree, including the root node. 

        for ind, n in list(enumerate(root)):
            if(ind == 0):
                node = Node(n)
                prevNode = node
                rootNode = node
                PrevChildren.append(node)
                allNodes.append(node)
                continue
            if(ind == len(root)-1):
                node = Node(n)
                children.append(node)
                prevNode.children = children
                allNodes.append(node)
                continue
            if(n == None):
                prevNode.children = children
                prevNode = PrevChildren[0]
                print([n.val for n in PrevChildren])
                print([n.val for n in children])
                PrevChildren.pop(0)
                children = []
                continue
            node = Node(n)
            children.append(node)
            PrevChildren.append(node)
            allNodes.append(node)  # all nodes of the tree, including the root node.
        print(rootNode.children)
        print([n.val for n in allNodes])
        for n in allNodes:
            if(n.children == None):
                continue
            print("The n value is: ", n.val)
            print("The nth value of node children: ", [j.val for j in n.children])
        nodes = Solution.inOrderInsert(rootNode)
        print("These are the nodes: ", nodes)
        return nodes

    def inOrderInsert(node, nodeList =[]):
        if(node.val == None):
            return None
        if(node.children==None or len(node.children) ==0):
            nodeList.append(node.val)
            return None
        nodeList.append(node.val)
        for child in node.children:
            Solution.inOrderInsert(child, nodeList)

        return nodeList

null = None
root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
answer = Solution.preorder(root)
print(answer)