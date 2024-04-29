class Solution:
    def isCircularSentence(sentence):
        def helper(sentence):
            words = sentence.split()
            checker = True
            for i in range(len(words)-1):
                if (words[i][-1] == words[i+1][0]):
                    continue
                else:
                    checker = False
                    break
            return checker
        if (sentence[0] == sentence[-1]):
            return True
        elif (helper(sentence)):
            return True
        else:
            return False
       
sentence = "leetcode exercises sound delightful"
sentence = "Leetcode is cool"
print(Solution.isCircularSentence(sentence)) # True