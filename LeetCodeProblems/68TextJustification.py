class Solution:
    def fullJustify(words, maxWidth):
        wordsList = []
        tempList = []
        size = 0
        #Step 1: Get a list of words with out spaces justified. 
        for ind, word in list(enumerate(words)):
            #print("Current word, size, and tempList is: ", word, size, tempList)
            if(len(wordsList) > 0):
                size += 1
            size += len(word)
            if(size > maxWidth):
                size = 0
                wordsList.append(tempList)
                #print("WordsList appended: ", tempList)
                tempList = []
                tempList.append(word)
                size += len(word)
                if(ind == len(words)-1):
                    wordsList.append(tempList)
                continue
            tempList.append(word)
            if(size > maxWidth):
                size = 0
                wordsList.append(tempList)
                #print("WordsList appended: ", tempList)
                tempList = []
                tempList.append(word)
                size += len(word)
                if(ind == len(words)-1):
                    wordsList.append(tempList)
                    #print("WordsList appended: ", tempList)
                continue

            if(ind == len(words)-1):
                wordsList.append(tempList)
                #print("WordsList appended: ", tempList)

        #Step 2: Get the count for each list of Words
        listWords = []
        for wl in wordsList:
            tempWord = ""
            for wIdx, w in list(enumerate(wl)):
                tempWord += w
                if (wIdx==len(wl)-1):
                    listWords.append(tempWord)
                    continue
                tempWord += " "
        #print(listWords)
        print("This is a wordsList: ", wordsList)
        tupList = []
        for x in listWords:
            tupList.append((x, len(x)))
        print("This is a tupList: ", tupList)

        #Step 3 get the answer List from the above two Lists.
        ansList = []
        for y in range(len(wordsList)):
            tempStr = ""
            #print("Current TupList is: ", tupList[y])
            #For end index justify left and only put extra spaces at the end. THIS PART WORKS
            if(y == (len(wordsList) - 1)):
                tempStr += tupList[y][0]
                remainingSpaces = (maxWidth - tupList[y][1]) * ' '
                #print("Remaining Spaces", remainingSpaces, "here")
                tempStr += remainingSpaces
                ansList.append(tempStr)
                break

            gaps = len(wordsList[y]) - 1
            wordsSize = 0
            for wrd in wordsList[y]:
                wordsSize += len(wrd)
            #print("Current wordsSize is: ", wordsSize)
            if((maxWidth - wordsSize) % gaps == 0):
                addedSpace = ' ' * ((maxWidth - wordsSize)//gaps)
                for wd in wordsList[y]:
                    tempStr += wd
                    if(len(tempStr) == maxWidth):
                        break
                    tempStr += addedSpace
                ansList.append(tempStr)
                continue
            remainderSpace = (maxWidth - wordsSize) % gaps
            #print("The remaining space is: ", remainderSpace)
            addedSpace = ' ' * ((maxWidth - wordsSize - remainderSpace)//gaps)
            for idx, wd in list(enumerate(wordsList[y])):
                if(idx == 0):
                    tempStr += wd
                    if(len(tempStr) == maxWidth):
                        break
                    tempStr += addedSpace
                    tempStr += ' ' * remainderSpace
                    continue
                tempStr += wd
                if(len(tempStr) == maxWidth):
                    break
                tempStr += addedSpace
            ansList.append(tempStr)
            continue


        #print(len(ansList[0]))
        return ansList
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

#words = ["What","must","be","acknowledgment","shall","be"]
#maxWidth = 16

answer = Solution.fullJustify(words, maxWidth)

print(answer)