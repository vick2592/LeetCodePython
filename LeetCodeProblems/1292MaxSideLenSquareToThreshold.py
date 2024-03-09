class Solution:
    def maxSideLength(mat, threshold):
        top = 0
        def helper(mat, i, j, k):
            if(i+k > len(mat) or j+k > len(mat[0])): return 0
            count = 0
            for x in range(i, i+k):
                for y in range(j, j+k):
                    count += mat[x][y]
            return count
        if(len(mat) > len(mat[0])): rng = len(mat[0])
        else: rng = len(mat)
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                for z in range(rng):
                    if(helper(mat, x, y, z) <= threshold):
                        top = max(top, z)
        return top

mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
threshold = 4
ans = Solution.maxSideLength(mat, threshold)
print(ans)
