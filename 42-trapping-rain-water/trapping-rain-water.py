class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, total, l_m, r_m = 0, len(height)-1, 0, 0, 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > l_m:
                    l_m = height[l]
                else:
                    total += l_m - height[l]
                l += 1
            else:
                if height[r] > r_m:
                    r_m = height[r]
                else:
                    total += r_m - height[r]
                r -= 1
        return(total)