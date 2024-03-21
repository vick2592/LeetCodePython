#from copy import deepcopy

class Solution:
    def evaluate(self, expression: str) -> int:

        def parse(e: str) -> list[str]:
            tokens, s, parenthesis = [], '', 0

            for c in e:
                if c == '(':
                    parenthesis += 1
                elif c == ')':
                    parenthesis -= 1
                    
                if parenthesis == 0 and c == ' ':
                    tokens.append(s)
                    s = ''
                else:
                    s += c

            if s: 
                tokens.append(s)
            
            return tokens

        def evaluate_expression(e: str, prevScope: dict) -> int:
            if e[0].isdigit() or e[0] == '-':
                return int(e)
            if e in prevScope:
                return prevScope[e]

            scope = prevScope.copy()
            nextExpression = e[e.index(' ') + 1:-1]
            print(e.index(' ') + 1)
            tokens = parse(nextExpression)
            print(tokens)
            if e[1] == 'a':
                return evaluate_expression(tokens[0], scope) + evaluate_expression(tokens[1], scope)
            if e[1] == 'm':
                return evaluate_expression(tokens[0], scope) * evaluate_expression(tokens[1], scope)

            for i in range(0, len(tokens) - 2, 2):
                scope[tokens[i]] = evaluate_expression(tokens[i + 1], scope)

            return evaluate_expression(tokens[-1], scope)

        return evaluate_expression(expression, {})

        
expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
ans = Solution()

print(ans.evaluate(expression))  # Output: 14
        

