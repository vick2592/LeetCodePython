class Solution:
    def numFactoredBinaryTrees(arr):
        mod = 10**9 + 7
        test = sorted(arr, reverse = True)
        print(test)
        count = len(arr)
        for x in range(len(test)-1):
            for y in range(x+1, len(test)):
                test1 = test[x] / test[y]
                if test1 in arr:
                    count += 1
                    print(test1)
        ans = count % mod
        return ans
    
arr = [2,4,5,10]
print(Solution.numFactoredBinaryTrees(arr)) #7