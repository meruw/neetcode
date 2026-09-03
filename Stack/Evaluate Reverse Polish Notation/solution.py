class Solution:
    def PolishNotation(self, tokens: list[str]) -> int:
        operators = {"+", "-", "*", "/"}
        operands: list[int] = []

        for x in tokens:
            if x in operators:
                print(operands)
                right = operands.pop()
                left = operands.pop()
                print(operands)

                if x == "+":
                    operands.append(left + right)
                    print(operands)
                elif x == "-":
                    operands.append(left - right)
                    print(operands)
                elif x == "/":
                    operands.append(int(left / right))
                    print(operands)
                elif x == "*":
                    operands.append(left * right)
                    print(operands)

            else: #number
                operands.append(int(x))
                print(operands)
        return operands[0]






s = Solution()
print(s.PolishNotation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
