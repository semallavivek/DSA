class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        l = 0
        temp = 0
        ans = 0
        for r in range(len(nums)):
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            temp += nums[r]
            if (r - l + 1 > k):
                temp -= nums[l]
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            if r - l + 1 == k and len(freq) == k:
                ans = max(ans, temp)
        return ans             
        