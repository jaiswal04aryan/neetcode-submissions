class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operationStack = [tokens[0]]
        if len(tokens) == 1:
            return int(tokens[0])
        operations = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in operations:
                operationStack.append(i)
            else:
                second = int(operationStack[-1])
                operationStack.pop()
                first = int(operationStack[-1])
                operationStack.pop()
                if i == "+":
                    operationStack.append(first + second)
                elif i == "-":
                    operationStack.append(first - second)
                elif i == "*":
                    operationStack.append(first * second)
                elif i == "/":
                    operationStack.append(first / second)
        return int(operationStack[-1])


        