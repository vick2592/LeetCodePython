class Solution:
    @staticmethod
    def buildMatrix(k, rowConditions, colConditions):
        mtrx = [[0]*k for _ in range(k)]

        def find_position_in_matrix(matrix, value):
            for i, row in enumerate(matrix):
                if value in row:
                    return (i, row.index(value))
            return None

        def isValid(matrix, rowConditions, colConditions, kTest):
            for i in range(1, kTest+1):
                pos = find_position_in_matrix(matrix, i)
                if pos is None:
                    return False
            # Validate row conditions
            for a, b in rowConditions:
                posA = find_position_in_matrix(matrix, a)
                posB = find_position_in_matrix(matrix, b)
                if posA and posB and posA[0] >= posB[0]:
                    return False
            # Validate column conditions
            for a, b in colConditions:
                posA = find_position_in_matrix(matrix, a)
                posB = find_position_in_matrix(matrix, b)
                if posA and posB and posA[1] >= posB[1]:
                    return False
            return True

        def dfs(matrix, cell=0):
            # print(matrix)
            if cell == k*k:
                if isValid(matrix, rowConditions, colConditions, k):
                    return [row[:] for row in matrix]
                return None

            r, c = divmod(cell, k)
            for val in range(0, k+1):
                matrix[r][c] = val
                result = dfs(matrix, cell + 1)
                if result is not None:
                    return result
                matrix[r][c] = 0  # Backtrack
            return None

        ans = dfs(mtrx)
        return ans if ans is not None else []

# Example usage
k = 3
rowConditions = [[1,2],[3,2]]
colConditions = [[2,1],[3,2]]
ans = Solution.buildMatrix(k, rowConditions, colConditions)
print(ans)