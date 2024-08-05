class Solution:
    def longestPalindrome(s):
        letterCount = {}
        for letter in s:
            if letter in letterCount:
                letterCount[letter] += 1
            else:
                letterCount[letter] = 1
        count = 0
        oneIn = False
        for l in letterCount:
            if letterCount[l] % 2 == 0:
                count += letterCount[l]
            elif oneIn == False:
                count += letterCount[l]
                oneIn = True
                
        print(letterCount)
        return count
    
s = "abccccdd"
answer = Solution.longestPalindrome(s)
print(answer)  # Expected output: 7
        