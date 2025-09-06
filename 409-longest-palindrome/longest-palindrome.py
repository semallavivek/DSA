from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        f = Counter(s)
        l = 0
        odd = False

        for count in f.values():
            if count % 2 == 0:
                l += count
            else:
                l += count - 1
                odd = True
        
        if odd:
            l += 1
        return l

        