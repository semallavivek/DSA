class Solution:
    def calculate(self, s: str) -> int:
        def eval_expr(it):
            stack = []
            num = 0
            sign = '+'
            while it[0] < len(s):
                ch = s[it[0]]
                if ch.isdigit():
                    num = num * 10 + int(ch)
                if ch == '(':
                    it[0] += 1
                    num = eval_expr(it)
                if (not ch.isdigit() and ch != ' ') or it[0] == len(s) - 1:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] *= num
                    elif sign == '/':
                        stack[-1] = int(stack[-1] / num)  # truncate toward zero
                    sign = ch
                    num = 0
                if ch == ')':
                    break
                it[0] += 1
            return sum(stack)

        return eval_expr([0])
