class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        le = 0

        while i >= 0 and s[i] == ' ':
            i -= 1
        
        while i >= 0 and s[i] != ' ':
            le += 1
            i -= 1
        return le