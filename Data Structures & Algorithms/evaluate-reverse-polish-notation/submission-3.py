class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            stack.append(token)
            match stack.pop():
                case "+":
                    o1 = int(stack.pop())
                    o2 = int(stack.pop())
                    stack.append(o2 + o1)
                case "*":
                    o1 = int(stack.pop())
                    o2 = int(stack.pop())
                    stack.append(o2 * o1)
                case "-":
                    o1 = int(stack.pop())
                    o2 = int(stack.pop())
                    stack.append(o2 - o1)
                case "/":
                    o1 = int(stack.pop())
                    o2 = int(stack.pop())
                    stack.append(int(o2 / o1))
                case _:
                    stack.append(int(token))
        return stack.pop()
