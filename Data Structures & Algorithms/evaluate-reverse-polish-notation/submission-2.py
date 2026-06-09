class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:

            if t.lstrip('-').isdigit():
                stack.append(int(t))
            elif t == '+':
                sec = stack.pop()
                first = stack.pop()
                stack.append(first+sec)
            elif t == '-':
                sec = stack.pop()
                first = stack.pop()
                stack.append(first-sec)
            elif t == '/':
                sec = stack.pop()
                first = stack.pop()
                stack.append(int(first/sec))
            else:
                sec = stack.pop()
                first = stack.pop()
                stack.append(first*sec)
            print(stack)

        return stack[-1]
        