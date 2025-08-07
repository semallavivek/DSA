class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        ans = 0
        dici = {}
        for r in range(len(s)):
            if s[r] not in dici:
                dici[s[r]] = 1
            else:
                while s[r] in dici:
                    del dici[s[l]]
                    l += 1
                dici[s[r]] = 1
            ans = max(ans, r-l+1)
        return ans