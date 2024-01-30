class Solution:
    def isPrefixOfWord(sentence, searchWord):
        sentence = sentence.split(" ")
        for i in range(0, len(sentence)):
            if sentence[i].startswith(searchWord):
                return i+1
        return -1
    
sentence = "i love eating burger"
searchWord = "burg"
print(Solution.isPrefixOfWord(sentence, searchWord))

