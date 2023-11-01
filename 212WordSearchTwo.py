from copy import deepcopy

class Solution:
    def findWords(board, words):
        xSize = len(board)
        ySize = len(board[0])
        validWords = []
        for word in words:
            tempWord = list(deepcopy(word))
            enumWord = list(enumerate(tempWord))
            #print("The enum version of word is: ", enumWord)
            tempInd = []
            print("Current iteration word is: ",tempWord)
            for x in range(xSize):
                if (word in validWords):
                    break
                for y in range(ySize):
                    #print("Current index x and y: ", x, y)
                    if(len(tempWord) == 0):
                        validWords.append(word)
                        break
                    if(board[x][y] == tempWord[0]):
                        tempInd.append((x,y))
                       # tempWord.pop(tempWord.index(board[x][y]))
                        tempX = x 
                        tempY = y
                        pq = []
                        pq.append((x,y,tempWord.index(board[x][y])))
                        #print("pq is: ", pq)
                        #Check if word sequentially possible from given index
                        while(True):
                            if(len(pq) == 0):
                                print("Nothing matched requirements for word")
                                break
                            #Prioritize queue
                            sorted(pq, key = lambda x: x[2], reverse = False)
                            print("sorted pq is: ", pq)
                            curInd = pq[0]
                            pq.pop(0)
                            #Check X value minus 1 or grid up
                            #From where I am, the question now becomes if this takes curIndex and then indexes the result from there there by
                            #in the pq the word index is prioritized by last and its according index.
                            if(curInd[0]-1 >= 0):
                                if (board[curInd[0]-1][curInd[1]] == tempWord[curInd[2]+1] and (curInd[0]-1, curInd[1]) not in tempInd ):
                                    tempInd.append((curInd[0]-1, curInd[1]))
                                    pq.append((curInd[0]-1, curInd[1],tempWord.index(board[curInd[0]-1][curInd[1]], curInd[2]+1)))
                                    sorted(pq, key = lambda x: x[2], reverse = False)
                                    print("sorted pq is: ", pq)
                                    if(pq[0][2] == len(tempWord)-1):
                                        print("Word has matched with final index: ", curInd[0]-1, curInd[1])
                                        tempWord = [] 
                                        break
                            #Check X value plus 1 or grid down
                            if(curInd[0]+1 < xSize):
                                if (board[curInd[0]+1][curInd[1]] == tempWord[curInd[2]+1] and (curInd[0]+1, curInd[1]) not in tempInd ):
                                    tempInd.append((curInd[0]+1, curInd[1]))
                                    pq.append((curInd[0]+1, curInd[1],tempWord.index(board[curInd[0]+1][curInd[1]], curInd[2]+1)))
                                    sorted(pq, key = lambda x: x[2], reverse = False)
                                    print("sorted pq is: ", pq)
                                    if(pq[0][2] == len(tempWord)-1):
                                        print("Word has matched with final index: ", curInd[0]+1, curInd[1])
                                        tempWord = [] 
                                        break
                            #Check Y value plus 1 or move right one col        
                            if(curInd[1]-1 >= 0):
                                if (board[curInd[0]][curInd[1]-1] == tempWord[curInd[2]+1] and (curInd[0], curInd[1]-1) not in tempInd ):
                                    tempInd.append((curInd[0], curInd[1]-1))
                                    pq.append((curInd[0], curInd[1]-1,tempWord.index(board[curInd[0]][curInd[1]-1], curInd[2]+1)))
                                    sorted(pq, key = lambda x: x[2], reverse = False)
                                    print("sorted pq is: ", pq)
                                    if(pq[0][2] == len(tempWord)-1):
                                        print("Word has matched with final index: ", curInd[0], curInd[1]-1)
                                        tempWord = [] 
                                        break
                            #Check Y value plus 1 or move right one col        
                            if(curInd[1]+1 < ySize):
                                if (board[curInd[0]][curInd[1]+1] == tempWord[curInd[2]+1] and (curInd[0], curInd[1]+1) not in tempInd ):
                                    tempInd.append((curInd[0], curInd[1]+1))
                                    pq.append((curInd[0], curInd[1]+1,tempWord.index(board[curInd[0]][curInd[1]+1], curInd[2]+1)))
                                    sorted(pq, key = lambda x: x[2], reverse = False)
                                    print("sorted pq is: ", pq)
                                    if(pq[0][2] == len(tempWord)-1):
                                        print("Word has matched with final index: ", curInd[0], curInd[1]+1)
                                        tempWord = [] 
                                        break

        return validWords
board = [["o","a","a","n"],["e","a","t","e"],["i","h","h","r"],["i","f","l","v"]]
words = ["oaath","pea","eat","rain"]

answer = Solution.findWords(board, words)
print("The valid words are: ", answer)