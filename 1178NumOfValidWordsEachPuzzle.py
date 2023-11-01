class Solution:
    def findNumOfValidWords(words, puzzles):
        wordInside = False
        answerList = [] 
        for p in puzzles:
            print(p)
            count = 0
            for w in words:
                #print(w)
                for c in range(len(w)):
                    print(w[1])
                    if w[c] in p and p[0] in w:
                        wordInside = True;
                        continue
                    wordInside = False
                    break
                if wordInside == True: 
                    count += 1


                wordInside = False
                print(count)
            answerList.append(count)

        return answerList 

words = ["aaaa","asas","able","ability","actt","actor","access"] 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
answer = Solution.findNumOfValidWords(words, puzzles)
print(answer)