class Solution:
    def findOcurrences(text, first, second):
        answer = []
        fFound = False
        sFound = False
        for word in text.split():
            #print(answer)
            #print(word, first, second)
            if fFound and sFound:
                answer.append(word)
                fFound = False
                sFound = False
                continue
            if word == first:
                fFound = True
                #print("true")
                continue
            if word == second:
                sFound = True
                continue
        return answer



text = "alice is a good girl she is a good student"
first = "a"
second = "good"

answer = Solution.findOcurrences(text, first, second)
print(answer)