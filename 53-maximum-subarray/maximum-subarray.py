class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1 = nums[0]
        temp = nums[0]

        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], temp + nums[i]) 
            sum1 = max(sum1, temp)
        return(sum1)