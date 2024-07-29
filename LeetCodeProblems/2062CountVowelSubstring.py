class Solution:
    def countVowelSubstrings(word):
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                print(word[i:j])
                if len(word[i:j]) >= 5:
                    match = True
                    for k in vowels:
                        if k not in word[i:j]:
                            match = False
                    if match:
                        count += 1
        return count
    
word = "aeiouu"
answer = Solution.countVowelSubstrings(word)
print(answer)  # Expected output: 3


