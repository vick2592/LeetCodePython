class Solution:
    def evaluate(expression):
        return 0
    
expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
ans = Solution.evaluate(expression)
print(ans)  # Output: 14
        

