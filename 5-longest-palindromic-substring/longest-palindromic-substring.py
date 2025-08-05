class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        longest = ""
        for i in range(len(s)):
            odd = expand(s, i, i)
            if len(odd) > len(longest):
                longest = odd
            even = expand(s, i, i+1)
            if len(even) > len(longest):
                longest = even
        return longest
        