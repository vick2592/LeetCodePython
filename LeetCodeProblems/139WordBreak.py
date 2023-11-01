class Solution:
    def wordBreak(s, wordDict):
        sSize = len(s)

        for word in wordDict:
            pq = []
            idx = 0
            if (s[:len(word)] == word):
                pq.append((word,len(word)))
            else:
                continue
            while (True):
                #Initial move
                if (len(pq) == 0):
                    break
                print(pq)
                prevWord = pq[0]
                pq.pop(0)

                if(prevWord[1] == sSize):
                    return True 
                for chainWord in wordDict:
                    if(prevWord[1]+len(chainWord) > sSize):
                        continue
                    if (s[prevWord[1]:prevWord[1]+len(chainWord)] == chainWord):
                        pq.append((chainWord,prevWord[1]+len(chainWord)))


        return False

s = "applepenapple"
wordDict = ["apple","pen"]

#s = "catsandog"
#wordDict = ["cats","dog","sand","and","cat"]

answer = Solution.wordBreak(s, wordDict)
print(answer)