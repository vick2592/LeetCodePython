import re
from copy import deepcopy
class Solution:
    def spellchecker(wordlist, queries):
        answer = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        for x in range(len(queries)):
            if queries[x] in wordlist:
                answer.append(queries[x])
                continue
            temp = queries[x].lower()
            if temp in wordlist:
                answer.append(temp)
                continue
            temp = ""
            for y in range(len(queries[x])):
                if queries[x][y].lower() in vowels:
                    temp += "*"
                else:
                    temp += queries[x][y]
            print("The current temp is: " + temp + "")
            match = False
            for wrd in wordlist:
                tempWrd = wrd.lower()
                tempWrd = re.sub(r'[a,e,i,o,u]', '*', tempWrd)
                originalTemp = deepcopy(queries[x])
                originalTemp = re.sub(r'[a,e,i,o,u]', '*', originalTemp)
                print("tempwrd, word, and originalword are: ", tempWrd, wrd, originalTemp)
                if originalTemp == tempWrd:
                    print("The word has been appended: ", wrd)
                    answer.append(wrd)
                    match = True
                    break
            if match:
                continue
            answer.append("")

        return answer
wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

answerList = Solution.spellchecker(wordlist, queries)
print(answerList)