class Solution:
    def countPairs(deliciousness):
        count = 0
        for x in range(len(deliciousness)):
            for y in range(x+1, len(deliciousness)):
                n = deliciousness[x] + deliciousness[y]
                if ((n>0 and ((n & (n-1)) == 0))):
                    count += 1

        return count
deliciousness = [1,1,1,3,3,3,7]
answer = Solution.countPairs(deliciousness)
print(answer)