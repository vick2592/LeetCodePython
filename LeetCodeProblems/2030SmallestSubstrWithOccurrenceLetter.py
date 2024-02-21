class Solution:
    def smallestSubsequence(s, k, letter, repetition):
        dp = []
        def dps(ind, k, strng, word = ""):
            if len(word) == k:
                dp.append(word)
                return
            if ind >= len(strng):
                return
            dps(ind + 1, k, strng, word)
            dps(ind + 1, k, strng, word + strng[ind])
            
        dps(0, k, s)
        # print(dp)
        ans = []
        for w in dp:
            count = 0
            for i in w:
                if i == letter:
                    count += 1
                if count == repetition:
                    ans.append(w)
                    break
        print(ans)
        ans = sorted(ans)
        return ans[0]
    
s = "leetcode"
k = 4
letter = "e"
repetition = 2

ans = Solution.smallestSubsequence(s, k, letter, repetition)
print(ans)
