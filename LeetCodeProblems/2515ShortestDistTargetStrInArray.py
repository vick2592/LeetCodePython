class Solution:
    def closetTarget(words, target, startIndex):
        if target not in words:
            return -1
        else:
            minDistance = len(words)
            for i in range(len(words)):
                if words[i] == target:
                    minDistance = min(minDistance, abs(i - startIndex))
            reverseInd = [n for n in list(range(len(words)))]        
            for j in reverseInd[::-1]:
                print(j)
                if words[j] == target:
                    minDistance = min(minDistance, abs(j - startIndex))
            return minDistance
    

words = ["hello","i","am","leetcode","hello"]
target = "hello"
startIndex = 1

answer = Solution.closetTarget(words, target, startIndex)
print(answer)