class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        def calculator(a, b, op):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            elif op == '/':
                return int(a / b)
            else:
                raise Exception('Invalid operator')
                return -1
        
        for i in range(len(tokens)):
            if tokens[i] in operators:
                a = stack.pop()
                b = stack.pop()
                res = calculator(b, a, tokens[i])
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]

