class Solution:
    def minDeletionSize(strs):
        count = 0
        for x in range(len(strs)):
            for y in range(len(strs[x])):
                if x > 0:
                    if strs[x][y] < strs[x-1][y]:
                        count += 1
                        break
        return count
        
strs = ["cba","daf","ghi"]

ans = Solution.minDeletionSize(strs)
print(ans)