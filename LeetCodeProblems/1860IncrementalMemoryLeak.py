class Solution:
    def memLeak(memory1, memory2):
        x = 1
        while (memory1 >= x or memory2 >= x):
            if memory1 >= memory2:
                memory1 -= x
            else:
                memory2 -= x
            x += 1
        ans = [x, memory1, memory2]    
        return ans
    
memory1 = 8
memory2 = 11

ans = Solution.memLeak(memory1, memory2)
print(ans)