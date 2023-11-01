class Solution:
    def removeAnagrams(words):
        answerList = []
        for idx, word in list(enumerate(words)):
            if(idx == 0):
                answerList.append(word)
                continue
            tempDict = {}
            for c in word:
                if c not in tempDict.keys():
                    tempDict[c] = 1 
                else:
                    tempDict[c] += 1

            tempDict1 = {}
            for c in words[idx - 1]:
                if c not in tempDict1.keys():
                    tempDict1[c] = 1 
                else:
                    tempDict1[c] += 1

            print(tempDict, tempDict1)
            if(tempDict == tempDict1):
                continue
            else:
                answerList.append(word)

        return answerList

words = ["abba","baba","bbaa","cd","cd"]
answer = Solution.removeAnagrams(words)
print(answer)