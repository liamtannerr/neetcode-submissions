class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {}

        pairs[')'] = '('
        pairs['}'] = '{'
        pairs[']'] = '['

        for c in s:
            if c in pairs:
                if not stack:
                    return False
                if stack[len(stack) - 1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) != 0:
            return False

        return True


