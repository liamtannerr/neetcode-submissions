class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if not tokens:
            return 0

        stack = []

        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                num = stack.pop()
                curEval = stack.pop()
                if token == "+":
                     curEval = curEval + num 
                elif token == "-":
                    curEval = curEval - num
                elif token == "*":
                    curEval = curEval * num
                else:
                    curEval = int(float(curEval) / num)
                stack.append(curEval)
            else:
                num = int(token)
                stack.append(num)


        return stack.pop()
        