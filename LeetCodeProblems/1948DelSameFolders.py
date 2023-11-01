#Chat GPT Trie generated Solution to this problem from the C++ code.
from typing import List
from collections import defaultdict

class Node:
    def __init__(self, name):
        self.name = name
        self.next = defaultdict(Node)
        self.del_flag = False

class DelSameFolders:
    def __init__(self):
        self.seen = {}  # mapping from subfolder structure string to the first occurrence node.
        self.ans = []
        self.path = []
    
    def addPath(self, node, path):
        for folder in path:
            if folder not in node.next:
                node.next[folder] = Node(folder)
            node = node.next[folder]
    
    def dedupe(self, node):
        subfolder = ""
        for name, next_node in node.next.items():
            subfolder += self.dedupe(next_node)
            print("Current subfolder is: ", subfolder)
        if subfolder:
            if subfolder in self.seen:
                self.seen[subfolder].del_flag = node.del_flag = True
            else:
                self.seen[subfolder] = node
        
        return "(" + node.name + subfolder + ")"
    
    def getPath(self, node):
        if node.del_flag:
            return

        self.path.append(node.name)
        self.ans.append(self.path.copy())
        
        for name, next_node in node.next.items():
            self.getPath(next_node)
        
        self.path.pop()
    
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node("/")
        for path in paths:
            self.addPath(root, path)
        
        self.dedupe(root)
        for name, nxt in root.next.items():
            self.getPath(nxt)

        return self.ans

#My solution that does not work as well but is a quick and dirty interview solution to the 3 given examples. 
class Solution:
    def deleteDuplicateFolder(paths):
        #Sort the paths for longest directory first
        print("Original Path: ", paths)
        paths = sorted(paths, key = lambda x: len(x), reverse = True)
        print("Sorted path are: ", paths)
        def inPathF(pathOne, pathTwo):
            inside = False
            pathTwoStart = pathTwo[0]
            pathTwoPointer = 0
            pathTwoLen = len(pathTwo)
            for p in pathOne:
                if(p == pathTwo[pathTwoPointer]):
                    pathTwoPointer += 1
                    pathTwoLen -= 1
                if(pathTwoLen == 0):
                    inside = True
                    break

            return inside

        #First scan and mark all arrays that are needed for one hop of deletion and add them to a list.
        delItems = []
        for i in range(len(paths)):
            tempEnd = paths[i][-1]
            count = 0
            for j in range(len(paths)):
                inPath = False
                for pth in delItems:
                    #This is where the error stems from as the path needs to match sub directory
                    #testInside = inPathF(paths[j], pth)
                    #print("Current: ", testInside)
                    if(inPathF(pth, paths[j])):
                        #print("Current path within delItems: ", pth, delItems)
                        inPath = True
                        break
                if(inPath == True):
                    continue
                if i == j:
                    continue
                if(paths[j][-1] == tempEnd):
                    if(paths[j] not in delItems):
                        delItems.append(paths[j])
                        count += 1
                    if(len(paths[j]) > 1):
                        delItems.append(paths[j][:len(paths[j])-1])

            if(count > 0):
                if(paths[i] not in delItems):
                    delItems.append(paths[i])
                if(len(paths[i]) > 1):
                    delItems.append(paths[i][:len(paths[i])-1])
                break
            
        #print("The deletedItems list is: ", delItems)
        #Second use that list to delete all arrays and return.
        for itm in delItems:
            for idx, pt in list(enumerate(paths)):
                if itm == pt:
                    paths.pop(idx)
        return paths

paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
#paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
#paths = [["a","b"],["c","d"],["c"],["a"]]

answer = Solution.deleteDuplicateFolder(paths)
solution = DelSameFolders()
answerChatGPT = solution.deleteDuplicateFolder(paths)
print(answer)
print(answerChatGPT)