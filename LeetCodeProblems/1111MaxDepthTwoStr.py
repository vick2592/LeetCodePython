class Solution:
    def maxDepthAfterSplit(seq):
        A = []
        B = []
        last = ''
        for i, c in enumerate(seq):
            if c == '(' and last != c:
                A.append(i)
                last = c
            elif c == '(' and last == c:
                B.append(i)
                last = c
            elif c == ')' and last != c:
                A.append(i)
                last = c
            elif c == ')' and last == c:
                B.append(i)
                last = c

        print(A, B)
        ans = []
        for i in range(len(seq)):
            if i in A:
                ans.append(0)
            else:
                ans.append(1)
        return ans

seq = "()(())()"
ans = Solution.maxDepthAfterSplit(seq)
print(ans)  # [0,1,1,1,1,0]