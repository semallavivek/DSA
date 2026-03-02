class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        depth = 0
        addition = 0
        for ch in s:
            if ch == '(':
                depth += 1
            else:
                if depth > 0:
                    depth -= 1
                else:
                    addition += 1
        return addition + depth 

        