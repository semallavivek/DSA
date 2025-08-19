class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = [x for x in nums if x > 0]
        n = [x for x in nums if x < 0]
        r = []
        for i in range (len(p)):
            r.append(p[i])
            r.append(n[i])
        return r