class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        r = 0
        for char in columnTitle:
            v = ord(char) - ord('A') + 1
            r = r * 26 + v
        return r