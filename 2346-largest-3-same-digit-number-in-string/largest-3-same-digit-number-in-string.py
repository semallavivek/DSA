class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        ans = ""
        for i in range(len(nums) - 2):
            if (nums[i] == nums[i+1] == nums[i+2]):
                ans = max(ans, nums[i:i+3])
        return ans

