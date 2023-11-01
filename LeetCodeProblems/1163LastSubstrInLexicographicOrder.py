class Solution:
    def lastSubstring(s):
        comblist = [] 
        for i in range(len(s)):
            temp = ""
            for j in range(i,len(s)):
                temp += s[j]
                if(temp not in comblist):
                    comblist.append(temp)
        comblist.sort()
        print(comblist)
        return comblist[-1]
s = "leetcode"
answer = Solution.lastSubstring(s)
print(answer)