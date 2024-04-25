#Can be improved with dynamic programming.

class Solution:
    @staticmethod
    def minCost(n, cuts):
        sCuts = sorted(cuts)
        
        def helper(start, end, Rcuts):
            if not Rcuts:
                return 0
            
            min_cost = float('inf')
            for i, cut in enumerate(Rcuts):
                # Calculate the cost of the current cut
                cost = end - start
                # Recursively calculate the cost for the left and right parts
                left_cost = helper(start, cut, Rcuts[:i])
                right_cost = helper(cut, end, Rcuts[i+1:])
                # Update the minimum cost
                min_cost = min(min_cost, cost + left_cost + right_cost)
            
            return min_cost

        return helper(0, n, sCuts)
        
    
n = 9
cuts = [5,6,1,4,2]

# n = 7
# cuts = [1,3,4,5]

print(Solution.minCost(n, cuts)) # 22

