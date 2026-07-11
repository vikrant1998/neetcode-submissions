class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack = deque()
        i = 0
        while i < len(s):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0: return False
                element = stack.pop()
                cond1 = (s[i] == ')') and element == '('
                cond2 = (s[i] == '}') and element == '{'
                cond3 = (s[i] == ']') and element == '['

                if not (cond1 or cond2 or cond3):
                    return False

            i += 1
        if len(stack) > 0:
            return False
        return True