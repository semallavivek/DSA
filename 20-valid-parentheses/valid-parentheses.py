class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        correct = {')' : '(',
                   ']' : '[',
                   '}' : '{'}
        for c in s:
            if c in correct:
                peek = stack.pop() if stack else '#'
                if correct[c] != peek:
                    return False
            else:
                stack.append(c)
        return not stack