class Solution:
    def containsPattern(arr, m, k):
        for x in range(len(arr)-m):
            test = arr[x:x+m]
            testK = k
            for y in range(x+m, len(arr)-m):
                if test == arr[y:y+m]:
                    k -= 1
                    y += m
                if k == 0:
                    return True
                
        return False
    
arr = [1,2,1,2,1,1,1,3]
m = 2
k = 2
# arr = [1,2,1,2,1,3]
# m = 2
# k = 3
answer = Solution.containsPattern(arr, m, k)
print(answer)