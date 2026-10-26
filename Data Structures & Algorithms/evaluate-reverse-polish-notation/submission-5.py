class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    o1 = stack.pop()
                    o2 = stack.pop()
                    stack.append(o2 + o1)
                case "*":
                    o1 = stack.pop()
                    o2 = stack.pop()
                    stack.append(o2 * o1)
                case "-":
                    o1 = stack.pop()
                    o2 = stack.pop()
                    stack.append(o2 - o1)
                case "/":
                    o1 = stack.pop()
                    o2 = stack.pop()
                    stack.append(int(o2 / o1))
                case _:
                    stack.append(int(token))
        return stack.pop()
