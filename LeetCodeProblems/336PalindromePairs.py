class Solution:
    def palindromePairs(words):
        def checkPalindrome(word):
            return word == word[::-1]
        ans = []
        for x in range(len(words) - 1):
            for y in range(x + 1, len(words)):
                test = words[x] + words[y]
                if checkPalindrome(test):
                    ans.append([x, y])
                test2 = words[y] + words[x]
                if checkPalindrome(test2):
                    ans.append([y, x])
        
        return ans


words = ["bat","tab","cat"]
words = ["abcd","dcba","lls","s","sssll"]
print(Solution.palindromePairs(words)) #[[0,1],[1,0]]
        