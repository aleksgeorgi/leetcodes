class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ""
        right = ""
        left = ""
        stack = []
        ops = "+-*/"

        for i in range(len(tokens)):
            if (tokens[i] in ops) and stack:
                right = stack.pop()
                left = stack.pop()
                if tokens[i] == "/":
                    op = tokens[i]
                    result = trunc(eval(left+op+right))
                    stack.append(str(result))
                else:
                    op = tokens[i]
                    result = eval(left+op+right)
                    stack.append(str(result))
            else:
                stack.append(tokens[i])

        return int(stack.pop())