class Solution:
    def nextGreatestLetter(letters, target):
        for i in letters:
            if i > target:
                return i
        return letters[0]


letters = ["c","f","j"]
target = "a"

answer = Solution.nextGreatestLetter(letters, target)
print(answer)