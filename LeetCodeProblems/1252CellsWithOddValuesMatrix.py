class Solution:
    def oddCells(m, n, indices):
                # Initialize a matrix with zeros
        matrix = [[0] * n for _ in range(m)]
        
        # Apply the increments
        for r, c in indices:
            for i in range(n):
                matrix[r][i] += 1
            for i in range(m):
                matrix[i][c] += 1
        
        # Count the number of cells with odd values
        odd_count = sum(cell % 2 != 0 for row in matrix for cell in row)
        
        return odd_count


m = 2
n = 3
indices = [[0,1],[1,1]]

answer = Solution.oddCells(m, n, indices)
print(answer)  # Expected output: 6