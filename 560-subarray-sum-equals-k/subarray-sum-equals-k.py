from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count =  0
        prefix = defaultdict(int)
        prefix[0] = 1
        s = 0

        for num in nums:
            s += num
            count += prefix[s-k]
            prefix[s] += 1
        return count
            