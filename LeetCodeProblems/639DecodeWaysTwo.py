class Solution:
    def numDecodings(self, s):
        mod = 10**9 + 7
        twoways = [n for n in range(11,27)]
        oneway = [n for n in range(1,11)]
        count = 0
        queue = []
        for i in range(len(s)):
            if s[i] != "*":
                if int(s[i]) == 0:
                    continue
            elif len(s) - i - 1 > 0 and s[i+1] != "*":
                if int(s[i]+s[i+1]) in twoways:
                    queue.append(int(s[i]))
                    queue.append(int(s[i] + s[i+1]))
                if int(s[i]+s[i+1]) in oneway:
                    queue.append(int(s[i]+s[i+1]))
            elif s[i] == "*":
                queue.append(1)
                queue.append(2)
                queue.append(3)
                queue.append(4)
                queue.append(5)
                queue.append(6)
                queue.append(7)
                queue.append(8)
                queue.append(9)
            elif len(s) - i - 1 > 0 and s[i+1] == "*":
                if s[i] == "1":
                    queue.append(11)
                    queue.append(12)
                    queue.append(13)
                    queue.append(14)
                    queue.append(15)
                    queue.append(16)
                    queue.append(17)
                    queue.append(18)
                    queue.append(19)
                elif s[i] == "2":
                    queue.append(21)
                    queue.append(22)
                    queue.append(23)
                    queue.append(24)
                    queue.append(25)
                    queue.append(26)   
            else:
                queue.append(int(s[i]))
        print(queue)
        
        return len(queue) % mod
    
s = "*"
ans = Solution()
print(ans.numDecodings(s))