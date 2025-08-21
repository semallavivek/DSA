class Solution:
    def toLowerCase(self, s: str) -> str:
        r = []
        for char in s:
            ascii = ord(char)
            if 65 <= ascii <= 90:
                r.append(chr(ascii + 32))
            else:
                r.append(char)
        return "".join(r)