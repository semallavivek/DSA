from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
     
        s_dici = Counter(s)
        t_dici = Counter(t)

        return(s_dici ==  t_dici)