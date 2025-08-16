class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_val = start ^ goal
        return bin(xor_val).count("1")