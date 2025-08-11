class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        m_a = 0
        while l <= r:
            w = r - l
            min_h = min(height[l], height[r])
            area = w * min_h
            m_a = max(m_a, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return m_a