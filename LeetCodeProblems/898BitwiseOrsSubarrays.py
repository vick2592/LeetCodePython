class Solution:
    def subarrayBitwiseORs(arr):
        res = set()
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                #test = [x for x ^ x+1 in arr[i:j+1]]
                test = 0
                for x in range(i, j+1):
                    test |= arr[x]
                res.add(test)
        return len(res)

arr = [1,1,2]
answer = Solution.subarrayBitwiseORs(arr)
print(answer)  # Expected output: 3