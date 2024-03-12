class Solution:
    def countExcellentPairs(nums, k):
        dp = {}
        count = 0
        tracker = []
        for x in range(len(nums)):
            for y in range(len(nums)):
                if dp.get((x, y), 0) == 0 and (nums[x], nums[y]) not in tracker:
                    countX = 0
                    countY = 0
                    tracker.append((nums[x], nums[y]))
                    for c in bin((nums[x] & nums[y])):
                        if c == '1':
                            countX += 1
                    for c in bin((nums[x] | nums[y])):
                        if c == '1':
                            countY += 1
                    dp[(x,y)] = countX + countY
        for v in dp.values():
            if v >= k:
                count += 1
                
        print(dp)
                

        return count
    

nums = [1,2,3,1]
k = 3
nums = [5,1,1]
k = 10
ans = Solution.countExcellentPairs(nums, k)
print(ans)  # Output: 0
    
