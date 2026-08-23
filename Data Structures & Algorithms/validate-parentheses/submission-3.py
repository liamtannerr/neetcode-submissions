class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {"(": ")",
                "[": "]",
                "{": "}"}
        print(pairs)
        for c in s:
            print(c)
            if c in pairs:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if not(pairs[top] == c):
                    return False

        return (not stack)