class Solution:
    def nthUglyNumber(n):
        count = 1
        ans = [1]
        while len(ans) < n:
            if count % 2 == 0 or count % 3 == 0 or count % 5 == 0:
                ans.append(count)
            count+=1
        print(ans)
        return ans[-1]
n = 10
ans = Solution.nthUglyNumber(n)
print(ans)

        