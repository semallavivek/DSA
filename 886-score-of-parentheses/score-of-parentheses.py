class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    inner_score = 0
                    while stack and stack[-1] != '(':
                        inner_score += stack.pop()
                    stack.pop()
                    stack.append(2*inner_score)
        return sum(stack)
