class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for s in tokens:
            if s not in operators:
                stack.append(s)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if s == '+':
                    stack.append(num1 + num2)
                elif s == '-':
                    stack.append(num1 - num2)
                elif s == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(num1 / num2)
        return int(stack[-1])