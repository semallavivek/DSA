from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        dici =  Counter(s)
        odd = float('-inf')
        even = float('inf')
        for i in dici.values():
            if i % 2 == 1:
                odd = max(odd, i)
            else:
                even = min(even, i)
        return odd - even